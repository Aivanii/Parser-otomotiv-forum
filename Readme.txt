`4 таска:
для получения данных конкретного юзера 
(айди, имя, ссылка на баннер, ссылка на аватарку, дату регистрации, кол-во сообщений, кол-во реакций, последняя активность, статус и роль)
нужно вызвать функцию getUserDataViaThreads файла linkGrabber, внутри функции getUserDataViaThreads в свою очередь используется функция getUserDataByUrl файла getUserData.

Сначала, метод getUserDataViaThreads собирает данные пользователей внутри первой страницы реестра, при помощи функции getUserDataByUrl (примечание: внутри getUserDataViaThreads по-умолчанию указана страница с реестром всех пользователей сайта otomotiv). Все ссылки полученные в процессе первого прохода заносятся внутрь локального массива. Это необходимо для предотвращения повторения данных из-за недавно зарегистрированных пользователей, которые всегда указаны в левой половине страницы, и пропуска ссылок на способы сортировки пользователей отличные от "зарегистрированных".

Важно заметить, что первыми проверяются ссылки на другие способы сортировки пользователей, отчего вход в аккаунт происходит чуть позже (в среднем через минуту). Вход происходит вручную.

После проверки первой страницы, метод getUserDataViaThreads, проходит по всем оставшимся страницам реестра пользователей и, на данный момент, сохраняет информацию в локальный массив.

Функция getUserDataViaThreads при безаварийной работе возвращает номер проверяемой страницы или ссылки на закрытые профили.
Функция getUserDataByUrl при успешном выполнении возвращает объект вида:
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
}`
