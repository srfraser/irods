import subprocess
        # test imeta -v
        imeta_popen = subprocess.Popen('echo "ls -d ' + irodshome + '/icmdtest/foo1" | imeta -v', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        imeta_output, imeta_err = imeta_popen.communicate()
        assert imeta_output.find('testmeta1') > -1
        assert imeta_output.find('180') > -1
        assert imeta_output.find('cm') > -1
        