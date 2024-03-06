import logging
logging.basicConfig(filename='sorting_logs.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import os
import shutil

output_folder = 'SORTED'
district_folders = [folder for folder in os.listdir() if os.path.isdir(folder)]

for district_folder in district_folders:
    try:
        district_number = os.path.basename(district_folder)

        zip_files = [f for f in os.listdir(district_folder) if
                     os.path.isfile(os.path.join(district_folder, f)) and f.endswith('.zip')]
        if not zip_files:
            logging.warning("Zip files not detected.")

        for zip_file in zip_files:
            temp_folder = os.path.join(district_folder, 'temp')
            shutil.unpack_archive(os.path.join(district_folder, zip_file), temp_folder, 'zip')
            logging.info(f"Unpacked zip: {zip_file}")
            for bank_folder_number in range(100):
                SheetType = f'T{bank_folder_number:02}_P01'
                bank_folder = os.path.join(temp_folder, 'el_info', 'bank', SheetType)
                if not bank_folder:
                    logging.warning("Zip does not have such a dir")
                if os.path.exists(bank_folder):
                    bank_folders = [f for f in os.listdir(bank_folder) if os.path.isdir(os.path.join(bank_folder, f))]

                    for bank_code in bank_folders:
                        output_bank_folder = os.path.join(output_folder, bank_code, SheetType)
                        os.makedirs(output_bank_folder, exist_ok=True)

                        shutil.copytree(os.path.join(bank_folder, bank_code),
                                        os.path.join(output_bank_folder), dirs_exist_ok=True)
        shutil.rmtree(temp_folder)
    except Exception as e:
        logging.error(f'An error occurred: {e}')
