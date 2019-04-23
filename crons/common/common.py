import hashlib

class common:

    # md5加密
    @staticmethod
    def  md5(str,slat=''):
        if(slat==''):
            slat = 'walkingsun'
        m = hashlib.md5()
        m.update(str.encode("utf-8"))  # md5对象里的update方法md5转换
        tmp = m.hexdigest() + slat
        m.update(tmp.encode("utf-8"))
        return m.hexdigest()