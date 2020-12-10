# import jenkinsapi
# from jenkinsapi.jenkins import Jenkins
import subprocess
from github import Github

# J = Jenkins('http://7ff862d678df.ngrok.io/')

last_build_Hashno = J['http:/localhost:8000/jtest'].get_last_good_build()

last_build_revNo = J['http:/localhost:8000/jtest'].get_last_good_build().get_revision()

print('Last #No. is [[%s]] and Rev No. is [[%s]]' % (last_build_Hashno, last_build_revNo))
# g=Github('800f2b5bc4a1d4b62a8f37e69abb7ecca3c00d1f')
# username='immdshahid'
# user=g.get_us
# print(subprocess.check_output(['git', last_build_revNo, 'C:/']))