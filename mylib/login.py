def userlogin(userid, userpw):
    check_result= False
    dbuserid='id1'
    dbuserpw='pw1'

    if userid== dbuserid:
        if userpw== dbuserpw:
            check_result= True
        else:
            pass
    else:
        pass

    return check_result