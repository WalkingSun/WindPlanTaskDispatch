from crontab import CronTab

class planServer:
    def __init__(self):
        pass

    def setCrons(self,cronsId, times, command):
        cron = CronTab(user=True)
        job = cron.new(command=command, comment=cronsId)
        job.setall(times)
        if (True == job.is_valid()):
            cron.write()
            job.enable(False)
            print("success")
            return True
        else:
            print("fail")
            raise Exception("crons命令语法不正确", 500)

    def delCrons(self,cronsId):
        cron = CronTab(user=True)
        # for job in cron:
        #     if job.comment == cronsId:
        #         cron.remove(job)
        #         cron.write()
        cron.remove_all( comment=cronsId)
        cron.write()
        return True

    def updateCrons(self,cronsId, times, command):
        cron = CronTab(user=True)
        for job in cron:
            if job.comment == cronsId:
                job.set_command(command)
                job.setall(times)
                if (True == job.is_valid()):
                    cron.write()
                    print('Cron job modified successfully')
                    return True
        return False
    def readCrons(self):
        cron = CronTab(user=True)
        res = ""
        for job in cron:
            res = res+str(job)+" | "
            print(job)
        return res

# setCrons(cronsId="WindSun1",times="*/1 * * * 1",command="ls")
# updateCrons(cronsId="WindSun1",times="*/3 * * * 1",command="ls")
# delCrons(cronsId="WindSun1")
# readCrons()