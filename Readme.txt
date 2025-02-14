4 таска:
для получения данных конкретного юзера 
(айди, имя, ссылка на баннер, ссылка на аватарку, дату регистрации, кол-во сообщений, кол-во реакций, последняя активность, статус и роль)
нужно вызвать функцию getUserDataByUrl файла getUserData с указанием url страницы пользователя
пример: print(getUserData.getUserDataByUrl('https://otomotiv-forum.com/members/bohdan.122109/' ))
ВАЖНО! В НАСТОЯЩЕЙ ВЕРСИИ КОДА НУЖНО ВХОДИТ В АККАУНТ ПЕРЕД ИЗВЛЕЧЕНИЕМ ДАННЫХ ВРУЧНУЮ ПОСЛЕ ЗАПУСКА КОДА!!!
Функция при успешном выполнении возвращает объект вида:
{
    ID: string,
    Name: string,
    Banner_URL: string,
    User_URL: string,
    Profile_Image_URL: string,
    Registration_Data: string,
    Message_Count: string,
    Reaction_Count: string,
    Last_Activity: string,
    Status: string,
    Roles: string,
}