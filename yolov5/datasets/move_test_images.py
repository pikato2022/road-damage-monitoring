import os
import errno
countries = ['Japan', 'India', 'Czech']
for test in ["test1", "test2"]:
    new_path = os.path.join(test, 'test_images')
    try:
        os.makedirs(new_path, exist_ok= True)
    except OSError as e:
        print("warning! {} already exists".format(new_path))
        if e.errno != errno.EEXIST:
            raise

    countries = os.listdir(test)
    for country in countries:
        if country not in countries :
            continue
        images_path = os.path.join(test, country, 'images')
        image_list = os.listdir(images_path)
        cmd = 'mv ' + images_path + ' ' + new_path
        print(cmd)
        os.system(cmd)