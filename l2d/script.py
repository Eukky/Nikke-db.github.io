import os 
import shutil
import fnmatch

source_path = os.path.abspath(r'E:\Nikke-db.github.io\l2d')


for root, dirs, files in os.walk(source_path):
   
    for folder in dirs:
        
        path = os.path.join(source_path, folder)
        # path = os.path.join(source_path, "777")
        for sub_root, sub_dirs, sub_files in os.walk(path):


            skel_name = ""
            atlas_name = ""
            png_name = ""

            print(sub_dirs)

            for sub_file in sub_files:
               
                if fnmatch.fnmatch(sub_file, '*.skel'):
                    skel_name = sub_file
                if fnmatch.fnmatch(sub_file, '*.atlas'):
                    atlas_name = sub_file
                if fnmatch.fnmatch(sub_file, '*.png'):
                    png_name = sub_file
            spine_name = skel_name.split(".")[0]
            # print(spine_name)
            # print(skel_name)
            # print(atlas_name)
            # print(png_name)

            f = open(folder + "/" + spine_name + ".config.json", "w")
            f.write('{\n')
            f.write('  "type": 9,\n')
            f.write('  "options": {\n')
            f.write('    "edge_padding": false\n')
            # f.write('    "spine_sdk": "4.1"\n')
            f.write('  },\n')
            f.write('  "skeleton": "%s",\n' % skel_name)
            f.write('  "atlases": [\n')
            f.write('    {\n')
            f.write('      "atlas": "%s",\n' % atlas_name)
            f.write('      "tex_names": [\n')
            f.write('        "%s"\n' % png_name.split(".")[0])
            f.write('      ],\n')
            f.write('      "textures": [\n')
            f.write('        "%s"\n' % png_name)
            f.write('      ]\n')
            f.write('    }\n')
            f.write('  ]\n')
            f.write('}')

            if len(sub_dirs) > 0 :
                path_aim = os.path.join(path, "aim")

                for sub_root1, sub_dirs1, sub_files1 in os.walk(path_aim):

                    skel_name = ""
                    atlas_name = ""
                    png_name = ""

                    print(sub_dirs1)

                    for sub_file1 in sub_files1:
                        if fnmatch.fnmatch(sub_file1, '*.skel'):
                            skel_name = sub_file1
                        if fnmatch.fnmatch(sub_file1, '*.atlas'):
                            atlas_name = sub_file1
                        if fnmatch.fnmatch(sub_file1, '*.png'):
                            png_name = sub_file1

                    spine_name = skel_name.split(".")[0]
                    # print(spine_name)
                    # print(skel_name)
                    # print(atlas_name)
                    # print(png_name)

                    f = open(folder + "/aim/" + spine_name + ".config.json", "w")
                    f.write('{\n')
                    f.write('  "type": 9,\n')
                    f.write('  "options": {\n')
                    f.write('    "edge_padding": false\n')
                    # f.write('    "spine_sdk": "4.1"\n')
                    f.write('  },\n')
                    f.write('  "skeleton": "%s",\n' % skel_name)
                    f.write('  "atlases": [\n')
                    f.write('    {\n')
                    f.write('      "atlas": "%s",\n' % atlas_name)
                    f.write('      "tex_names": [\n')
                    f.write('        "%s"\n' % png_name.split(".")[0])
                    f.write('      ],\n')
                    f.write('      "textures": [\n')
                    f.write('        "%s"\n' % png_name)
                    f.write('      ]\n')
                    f.write('    }\n')
                    f.write('  ]\n')
                    f.write('}')


                path_cover = os.path.join(path, "aim")

                for sub_root2, sub_dirs2, sub_files2 in os.walk(path_cover):

                    skel_name = ""
                    atlas_name = ""
                    png_name = ""

                    print(sub_dirs2)

                    for sub_file2 in sub_files2:
                        if fnmatch.fnmatch(sub_file2, '*.skel'):
                            skel_name = sub_file2
                        if fnmatch.fnmatch(sub_file2, '*.atlas'):
                            atlas_name = sub_file2
                        if fnmatch.fnmatch(sub_file2, '*.png'):
                            png_name = sub_file2

                    spine_name = skel_name.split(".")[0]
                    # print(spine_name)
                    # print(skel_name)
                    # print(atlas_name)
                    # print(png_name)

                    f = open(folder + "/cover/" + spine_name + ".config.json", "w")
                    f.write('{\n')
                    f.write('  "type": 9,\n')
                    f.write('  "options": {\n')
                    f.write('    "edge_padding": false\n')
                    # f.write('    "spine_sdk": "4.1"\n')
                    f.write('  },\n')
                    f.write('  "skeleton": "%s",\n' % skel_name)
                    f.write('  "atlases": [\n')
                    f.write('    {\n')
                    f.write('      "atlas": "%s",\n' % atlas_name)
                    f.write('      "tex_names": [\n')
                    f.write('        "%s"\n' % png_name.split(".")[0])
                    f.write('      ],\n')
                    f.write('      "textures": [\n')
                    f.write('        "%s"\n' % png_name)
                    f.write('      ]\n')
                    f.write('    }\n')
                    f.write('  ]\n')
                    f.write('}')

        
