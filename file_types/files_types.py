import magic, os
f = magic.Magic(magic_file=r'F:\test\python\file_types\file\share\misc\magic',
            uncompress=True, mime=True)
path = r'D:\,\Default\New folder\Cache'
for file in os.listdir(path):    
    full_file_path = r'' + path + '\\' + file
    if os.path.isfile(full_file_path):
        type_name = f.from_file(full_file_path)
        file_ext = type_name.split('/')[1]
        os.rename(full_file_path, full_file_path + '.' + file_ext)

