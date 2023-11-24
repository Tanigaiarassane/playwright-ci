import jenkins
import sys
import os

jenkins_server = "http://localhost:8080"

def buildojobs(location):
    xml_files = [f for f in os.listdir(dir) if f.endswith('.xml')]
    print (xml_files)

    for file in xml_files:
        path = os.path.join(location,file)
        with open (path, 'r') as xml_file:
            xml_content = xml_file.read()
        create_jenkins_job(str(file).split('.'), xml_content)

def create_jenkins_job(jobname, xmlstr, reconfigure=false):
    # Create jenkins job
    print ("jobname: {} ".format(jobname))
    try:
        if server.job_exists(jobname):
            server.reconfigure_job(jobname, xmlstr)
        return True
        else:
            server.create_job(jobname, xmlstr)
        return True
    except:
        print ("Invalid jpb xml job {}".format(jobname))
        return false

if __name__ == "__main__":
    directory = sys.argv[1]
    job_action = buildjobs(str(directory))