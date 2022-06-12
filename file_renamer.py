import glob
import os
import re

class File_renamer:
    def execute(self, right_names, path, extension):
        os.chdir(path)
        renamed_files_count = 0
        for file in glob.glob("*" + extension):
            file_without_extension = file.split(extension)[0]
            forbidden_characters = r'[&*/:`<>?\|]'
            clean_file_name = re.sub(forbidden_characters, '_', file_without_extension)

            if (clean_file_name != file_without_extension):
                print("Forbidden character detected. Renaming...")
                os.rename(file_without_extension + extension, clean_file_name + extension)    

            key = clean_file_name.split("(")[0].strip().lower()
            if key in right_names:
                rightName = right_names[key] + extension
                if (file != rightName):
                    print(file + " -> " + rightName)
                    os.rename(clean_file_name + extension, rightName)
                    renamed_files_count+=1
        return renamed_files_count