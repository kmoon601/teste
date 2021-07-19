#사용자 이이디 비번 입력
# 변수에 저장하거나 바로비교

userid = 'id'
userpw= 'pw'

#사용자 정보가잇는 db에서 데이터를 가져와서
# 변수에 저장하고 비교
# 데이터 베이스 연결코드 작성( 함수로)

dbuserid= 'id'
dbuserpw= 'pw'

# db 아이디 비번과 아이디비번 비교
if userid == dbuserid:
    if userpw == dbuserpw:
        userid= "성공"
        # 로그인 성공후 다음 일처리 코드 작성
    else :
        userid= '실패'
    # 비밀번호 잘못입력햇는지 기록
else:
    userid =" 실패"
    # 아이디 잘못입력햇는지 기록
temp=0