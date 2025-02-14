import getUserData
import linkGrabber

# Profile page URL
##userUrl = 'https://otomotiv-forum.com/members/bohdan.122109/' 
##print(getUserData.getUserDataByUrl(userUrl))
linkGrabber.getUserDataViaThreads()

## changelog
##1. имплементировал получение данных в получатель ссылок
##2. вынес подключение драйвера за фукнцию получения данных
##3. добавил проверку на доступность страницы пользователя
##4. начал делать выгрузку пользователей из общего реестра

