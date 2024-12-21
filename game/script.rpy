# Определение персонажей игры.
define Jame = Character('Джейм', color="#77716d")
define unknown = Character('???', color="#a7a7a7")
define figure = Character('Фигура', color="#9b9b9b")
define Jame_thought = Character('Джейм (мысленно)', color="#77716d")
define Andrey = Character('Андрей', color="#6a7194")
define Glitch = Character('Глитч', color="#3082b5")
define Vanillope = Character('Ванилопа', color="#6fb7a1")
define Ralph = Character('Ральф', color="#c26448")
define Colleague = Character('Коллега', color="#a8a8a8")


define Friendship_Saves_the_World = 0
define The_Price_of_Mistrustt = 0
define Sacrifice_in_the_Name_of_Salvation = 0
define Lost_Opportunities = 0
define glitch = 0


label start:
    stop music fadeout .5
    play music calm_music 
    scene park with dissolve
    "{i}{alpha=*0.5}Темное утро. Небо затянуто серыми облаками, отражающими настроение Джейма. Он спешит по пустыннымому парку, держа в руке кружку горячего кофе."
    "{i}{alpha=*0.5}Его глаза слегка прикрыты, но он пытается выглядеть бодрым."
    "{i}{alpha=*0.5}Джейм, одетый в серую рубашку и брюки, подходит к офисному зданию, где работает специалистом по информационной безопасности." 
    "{i}{alpha=*0.5}В холле его приветствует охранник, но Джейм лишь кивает в ответ, погруженный в свои мысли."
    Jame_thought "Еще немного кофе, и я буду готов к новому дню. Сегодня нужно проверить систему безопасности... Надеюсь, никаких проблем не возникнет."
    window hide
    scene black with dissolve
    window show
    scene park with dissolve
    "{i}{alpha=*0.5}Решив пройтись через парк перед работой, он наслаждается свежим воздухом. Листья под ногами шуршат, и прохладный ветер освежает его лицо."
    "{i}{alpha=*0.5}Вдруг он замечает своего друга Андрея, который сидит на скамейке и смотрит на небо."
    show jame_idle at center with dissolve
    Jame "Привет, Андрей! Как дела?"
    "{i}{alpha=*0.5}Андрей поднимает взгляд и улыбается в ответ."
    show andrey_idle at right with dissolve
    Andrey "Привет, Джейм! Неплохо. А ты как?"
    hide jame_idle with dissolve
    show jame_sad with dissolve
    "{i}{alpha=*0.5}Джейм садится рядом, чувствуя странное беспокойство."
    Jame "Не знаю... У меня какое-то странное чувство сегодня. Как будто что-то не так."
    "{i}{alpha=*0.5} Андрей внимательно смотрит на него."
    Andrey "Может, переутомился? Ты много работаешь в последнее время."
    Jame "Может быть. Но это чувство не проходит."
    "{i}{alpha=*0.5}Андрей легонько толкает его плечом."
    Andrey "Давай зайдем в кафе, выпьем кофе. Может, это поможет."
    Jame "Почему бы и нет."
    "{i}{alpha=*0.5}Они направляются в близлежащее кафе. Внутри уютно, пахнет свежей выпечкой и молотым кофе. Они заказывают по чашке и садятся у окна."
    scene coffee with dissolve
    show jame_idle with dissolve
    show andrey_idle at right with dissolve
    "{i}{alpha=*0.5}Во время разговора Джейм замечает, что Андрей кажется немного отстраненным, но не придает этому значения."
    scene park with dissolve
    "{i}{alpha=*0.5}После кофе они выходят на улицу."
    show jame_idle with dissolve 
    show andrey_idle at right with dissolve
    Andrey "Мне пора бежать. Дела ждут."
    Jame "Конечно. Увидимся позже."
    "{i}{alpha=*0.5}Они обмениваются прощальными жестами, и Джейм направляется к своей работе."
    hide andrey_idle with dissolve
    Jame_thought "Почему это чувство не проходит? Как будто что-то важное должно случиться..."
    scene server with dissolve
    show jame_idle with dissolve
    "{i}{alpha=*0.5}Он приходит в серверную. Ряды серверов, мигающие индикаторы, тихий гул оборудования создают привычную атмосферу. Но что-то кажется неправильным."
    scene server_2 with dissolve
    stop music fadeout .5
    play music angry_music fadein .5
    "{i}{alpha=*0.5}Вдруг он замечает искры, исходящие из одного из серверов."
    Jame "Что за... Это опасно."
    "{i}{alpha=*0.5}Он подходит ближе, пытаясь разобраться в причине."
    scene server_light with dissolve
    "{i}{alpha=*0.5}Внезапно мощный электрический разряд озаряет комнату. Свет становится нестерпимо ярким, звук гудения усиливается." 
    "{i}{alpha=*0.5}Джейм пытается отойти, но его ноги не слушаются. Все вокруг начинает вращаться."
    hide jame_idle with dissolve
    show jame_scared with dissolve
    Jame "ЧТО ПРОИСХОДИТ?!"
    "{i}{alpha=*0.5}Мир вокруг него исчезает в яркой вспышке."
    jump part_2

    label part_2:
        stop music fadeout 3
        window hide
        scene black with dissolve
        pause 3
        scene wake_light with dissolve
        scene wake with dissolve
        window show
        play music sad_music_1 fadein 3
        "{i}{alpha=*0.5}Джейм медленно открывает глаза. Он лежит на земле, но она состоит из пикселей. Вокруг яркие цвета, нереальные формы." 
        "{i}{alpha=*0.5}Небо состоит из цифровых облаков, а деревья напоминают старые 8-битные игры."
        show jame2_sad at left with dissolve
        Jame "Где я?!"
        "{i}{alpha=*0.5}Рядом слышится голос."
        unknown "Смотри-ка, новый игрок!"
        "{i}{alpha=*0.5}Он поворачивает голову и видит перед собой девочку с короткими темными волосами и озорными глазами, одетую в яркий костюм."
        show vanillope at center with dissolve
        Vanillope "Привет! Я Ванилопа фон Кекс! А ты кто?"
        "{i}{alpha=*0.5}Рядом с ней стоит высокий мужчина с мощным телосложением."
        show ralph_idle at right with dissolve
        Ralph "Я Ральф. Ты в порядке?"
        "{i}{alpha=*0.5}Джейм пытается встать, чувствуя, как его тело кажется легким и необычным."
        Jame "Я... Я Джейм. Где я нахожусь?"
        "{i}{alpha=*0.5}Ванилопа смеется."
        Vanillope "Ты в нашей игре, конечно! Но ты не похож на обычного персонажа."
        "{i}{alpha=*0.5}Джейм смотрит на свои руки и замечает, что они тоже пиксельные."
        Jame "Это невозможно... Я был в серверной, и вдруг... Что происходит?"
        "{i}{alpha=*0.5}Ральф кладет руку ему на плечо."
        Ralph "Спокойно. Мы разберемся. Но сейчас у нас проблема посерьезнее."
        "{i}{alpha=*0.5}Ванилопа кивает."
        Vanillope "Наш мир атакован вирусом! Он разрушает игры и изменяет код. Ты можешь нам помочь?"
        window hide
        menu:
            "Согласиться помочь сразу.":
                window show
                $ Friendship_Saves_the_World += 1
                $ Sacrifice_in_the_Name_of_Salvation += 1
                hide jame2_sad with dissolve
                show jame2_idle at left with dissolve
                
                Jame "Конечно, я помогу. Расскажите подробнее, что происходит."
                Vanillope "Здорово! Я знала, что ты не откажешь!"
                Ralph "Спасибо. Вместе у нас больше шансов."
                "{i}{alpha=*0.5}Отношения с Ральфом и Ванилопой улучшаются. Они начинают доверять Джейму и охотно делятся информацией."
                Vanillope "Вирус появился неожиданно и начал менять код игр. Мы пытаемся найти источник, но без твоей помощи нам не обойтись."
                Ralph "Мы слышали о специалистах из реального мира. Возможно, твои знания помогут нам остановить эту угрозу."
                Jame "Я сделаю все, что в моих силах."
                "{i}{alpha=*0.5}Ванилопа хлопает в ладоши."
                Vanillope "Отлично! У нас появился новый союзник!"
                window hide
                scene black with dissolve
                pause 3
                scene city with dissolve
                window show
                "{i}{alpha=*0.5}Ребята решили устроить небольшой привал и обсудить план действий."
                "{i}{alpha=*0.5}Появилась возможность узнать о них побольше."
                "{i}{alpha=*0.5}Что спросить?"
                window hide
                menu:
                    "Спросить о их прошлом.":
                        window show
                        show jame2_idle with dissolve
                        show ralph_idle at right with dissolve
                        show vanillope at left with dissolve
                        Jame "Расскажите больше о себе."
                        Ralph "Я раньше был злодеем в своей игре, но теперь стараюсь быть хорошим парнем."
                        Vanillope "А я принцесса и гонщица! Люблю приключения!"

                    "Сосредоточиться на плане.":
                        window show   
                        show jame2_idle with dissolve
                        show ralph_idle at right with dissolve
                        Jame "Давайте еще раз обсудим наш план."
                        Ralph "Хорошо. Нам нужно быть готовыми ко всему."

                jump part_3
            "Сомневаться и попросить больше информации.":
                window show
                $ The_Price_of_Mistrustt +=1 
                $ Lost_Opportunities += 1
                hide jame2_sad with dissolve
                show jame2_idle at left with dissolve
                Jame "Погодите, я даже не понимаю, где я и что происходит. Расскажите подробнее."
                Vanillope "Ну, хорошо. Постараюсь объяснить."
                Ralph "Мы понимаем, что это сложно принять. Мы расскажем все, что знаем."
                "{i}{alpha=*0.5}Ральф и Ванилопа понимают сомнения Джейма, но чувствуют небольшое разочарование."
                Vanillope "Ладно, начнем с начала. Ты в цифровом мире, внутри игры."
                Ralph "Наш мир под угрозой из-за вируса. Мы ищем помощь, и ты можешь быть нашим шансом."
                Jame "Это все очень странно... Но если я могу помочь, я попробую."
                jump part_3

        

    label part_3:
        stop music fadeout 3
        window hide
        scene black with dissolve
        pause 3
        scene city with dissolve
        window show
        play music uplifting_music fadein 3
        "{i}{alpha=*0.5}Они идут по улицам игрового города. Повсюду хаос: персонажи застывают, здания мерцают и исчезают, небо меняет цвет."
        show jame2_idle with dissolve
        show vanillope at left with dissolve
        show ralph_idle at right with dissolve
        Jame "Вирус распространяется быстро. Если мы не остановим его, весь мир может исчезнуть."
        "{i}{alpha=*0.5}Ванилопа указывает вперед."
        Vanillope "Есть одно место, где мы можем найти ответы – Сектор Забытых Игр. Но это опасно."
        Ralph "Мы справимся. У нас нет выбора."
        "{i}{alpha=*0.5}Внезапно перед ними появляется загадочная фигура в плаще, скрывающая лицо."
        figure "Стойте. Дальше путь закрыт."
        "{i}{alpha=*0.5}Джейм делает шаг вперед."
        Jame "Кто ты?"
        "{i}{alpha=*0.5}Фигура снимает капюшон. Под ним девушка с пиксельными волосами и светящимися глазами."
        hide ralph_idle with dissolve
        show glitch at right with dissolve
        Glitch "Я Глитч. Я – ошибка в коде, но я могу помочь вам."
        Vanillope "Почему ты хочешь нам помочь?"
        Glitch "Вирус разрушает и меня. Если мы не остановим его, я исчезну навсегда. Взамен я прошу помочь мне найти мое истинное предназначение."
        Vanillope "Что скажешь, Джейм? Мы возьмем её с собой?"
        window hide
        menu:
            "Довериться Глитч":
                window show
                $ Friendship_Saves_the_World +=1
                $ Sacrifice_in_the_Name_of_Salvation += 1
                $ glitch += 1
                Jame "Мы ищем способ остановить вирус. Если ты можешь помочь, мы будем благодарны."
                Glitch "Я знаю эти места и могу провести вас безопасным путем."
                Ralph "Джейм, ты уверен?"
                Jame "Да. Нам нужна любая помощь."
                "{i}{alpha=*0.5}Глитч присоединяется к команде, предоставляет информацию о скрытых опасностях и коротких путях."
                Glitch "Вирус изменил многие пути. Но я знаю обходные маршруты."
                Vanillope "Здорово! С тобой нам будет проще."
                Ralph "Спасибо за помощь."
                "Ребята начинают свой путь."
                window hide
                scene black with dissolve
                pause 1
                scene city_2 with dissolve
                window show
                "Джейм замечает, что Глитч выглядит задумчиво."
                "Как реагировать?"
                window hide
                menu:
                    "Поддержать её.":
                        window show
                        show jame2_idle with dissolve
                        show glitch at right with dissolve
                        Jame "Все в порядке? Ты выглядишь обеспокоенной."
                        Glitch "Просто думаю о том, кто я на самом деле..."
                        Jame "Мы поможем тебе найти ответы."
                        "{i}{alpha=*0.5}Глитч благодарна, отношения улучшаются."
                    
                    "Игнорировать.":
                        window show
                        show jame2_idle with dissolve
                        show glitch at right with dissolve
                        Jame "Нам нужно двигаться дальше."
                        "{i}{alpha=*0.5}Глитч остаётся молчаливой."

                jump part_4

            "Не доверять Глитч": 
                window show
                $ The_Price_of_Mistrustt += 1
                $ Lost_Opportunities += 1
                Jame "Извини, но мы не можем доверять незнакомцам в такое время."
                Glitch "Понимаю. Желаю удачи."
                hide glitch with dissolve
                "{i}{alpha=*0.5}Глитч исчезает между аркадных автоматов и пиксельных руин."
                Vanillope "Джейм, а что теперь? Она знала обходные пути..."
                Ralph "Мы сами справимся. Но нам придётся искать старые указатели к порталу. Я слышал легенды, что некоторые забытые данные хранятся у истока — там, где ты, Джейм, появился."
                Jame "Значит, вернёмся к месту пробуждения. Возможно, я смогу проанализировать структуру кода там."
                jump part_4

    label part_4:

        if glitch > 0:
            stop music fadeout 3
            window hide
            scene black with dissolve
            pause 3
            scene city with dissolve
            window show
            play music badass_music fadein 3
            "{i}{alpha=*0.5}Они продолжают путь вместе. Глитч ведет их через скрытые проходы, обходя опасные зоны. По дороге они видят, как вирусные существа захватывают новые территории." 
            scene portal with dissolve
            "{i}{alpha=*0.5}Наконец они достигают центра Сектора Забытых Игр. Перед ними возвышается огромный портал, из которого исходит темная энергия."
            show glitch at right with dissolve
            Glitch "Это источник вируса."
            "{i}{alpha=*0.5}Из портала выходит фигура. Джейм узнает его."
            show jame2_idle at left with dissolve
            Jame "Андрей?!"
            show andrey_serious at center with dissolve
            Andrey "Привет, Джейм. Не ожидал тебя здесь увидеть."
            Vanillope "Это тот самый Андрей?"
            "{i}{alpha=*0.5}Ральф кивает, напрягаясь." 
            Jame "Что ты здесь делаешь? Почему ты это делаешь?"
            hide andrey_serious with dissolve
            show andrey_angry with dissolve
            Andrey "Всегда {b}ты{/b} был лучшим. Всегда впереди. Но теперь у меня есть шанс стать первым. С помощью этого вируса я стану властелином этого мира."
            Jame "Это безумие! Ты разрушишь все!"
            hide andrey_angry with dissolve
            show andrey_serious with dissolve
            Andrey "Мне все равно. Я устал быть в тени."
            "{i}{alpha=*0.5}Ральф делает шаг вперед."
            hide glitch with dissolve
            show ralph_idle at right with dissolve
            stop music fadeout .5
            play music epic_battle_music fadein .5
            Ralph "Мы не позволим тебе это сделать!"
            "{i}{alpha=*0.5}Начинается битва. Вирусные существа нападают на них. Ральф отбрасывает их мощными ударами, Ванилопа использует свою скорость, чтобы запутать врагов."
            "{i}{alpha=*0.5}Глитч пытается проникнуть в код вируса."
            hide ralph_idle with dissolve
            "{i}{alpha=*0.5}Джейм и Андрей стоят друг напротив друга."
            Jame "Пожалуйста, остановись. Это не выход."
            Andrey "Слишком поздно для разговоров."
            "{i}{alpha=*0.5}Они вступают в цифровую схватку. Джейм пытается взломать контроль Андрея над вирусом, но тот защищается."
            "{i}{alpha=*0.5}Внезапно Глитч кричит:"
            show glitch at right with dissolve
            Glitch "Джейм! Я могу помочь! Используй меня, чтобы разрушить вирус изнутри!"
            Jame "Но это может уничтожить тебя!"
            Glitch "Это мой выбор."
            "{i}{alpha=*0.5}Джейм соединяет Глитч с кодом вируса. Начинается мощный сбой. Вирус начинает разрушаться, система перегружается."
            hide glitch with dissolve
            hide andrey_serious with dissolve
            show andrey_angry with dissolve
            Andrey "Нет! Что ты сделал?!"
            "{i}{alpha=*0.5}Портал начинает коллапсировать. Ванилопа и Ральф бегут к выходу."
            show vanillope at right with dissolve
            Vanillope "Джейм! Пора уходить!"
            hide andrey_angry with dissolve
            show andrey_serious with dissolve
            stop music fadeout .5
            window hide
            play music sad_music_2 fadein .5
            Andrey "Все потеряно..."
            menu:
                "Попытаться спасти Андрея":
                    window show
                    $ Friendship_Saves_the_World += 1
                    $ The_Price_of_Mistrustt += 1
                    Jame "Я не оставлю тебя здесь! Давай, уходи со мной!"
                    Andrey "После всего, что я сделал?"
                    Jame "Мы друзья. Вместе мы все исправим."
                    "{i}{alpha=*0.5}Джейм протягивает руку, Андрей принимает ее, и они вместе выбираются."
                    "{i}{alpha=*0.5}Андрей осознает свои ошибки и помогает команде в последние минуты."
                    Andrey "Спасибо... Я поступил ужасно. Помогу вам исправить это."
                    "{i}{alpha=*0.5}Вместе они стабилизируют систему, вирус полностью уничтожен."
                    hide vanillope with dissolve
                    show glitch at right with dissolve
                    Glitch "Ваше прощение спасло нас всех."
                    hide jame2_idle with dissolve
                    show vanillope at left with dissolve
                    Vanillope "Рады, что ты с нами."
                    jump epilogue
                
                "Оставить Андрея":
                    window show
                    $ Sacrifice_in_the_Name_of_Salvation += 1
                    $ Lost_Opportunities += 1
                    Jame "Ты сам выбрал этот путь."
                    Andrey "Пожалуйста... Не бросай меня..."
                    Jame "Я не могу рисковать всеми ради тебя."
                    "{i}{alpha=*0.5}Джейм уходит, оставляя Андрея в разрушающемся портале."
                    window hide
                    scene black with dissolve
                    pause .5
                    scene portal with dissolve
                    show vanillope at center with dissolve
                    show ralph_idle at left with dissolve
                    show jame2_sad at right with dissolve
                    Vanillope "Мы могли бы попытаться спасти его..."
                    Ralph "Иногда приходится делать трудный выбор."
                    Jame "Давайте уйдем отсюда."
                    "{i}{alpha=*0.5}Вирус остановлен, но чувство вины остается."
                    jump epilogue

        else:
            window hide
            scene black with dissolve
            pause 3
            scene wake with dissolve
            window show
            show jame2_idle with dissolve
            show vanillope at left with dissolve
            show ralph_idle at right with dissolve
            "{i}{alpha=*0.5}Они возвращаются в точку, где Джейм впервые очнулся в цифровом мире."
            Vanillope "Не похоже, что тут есть что-то полезное..." 
            Ralph "Подожди. Я вижу странные линии кода, мерцающие внизу."
            Jame "Это фрагменты системных логов. Кажется, они указывают на место, где код наиболее искажён — Путь к центру вируса." 
            Jame "Если мы туда проберёмся, сможем добраться до портала и.… до того, кто за всем стоит."
            Vanillope "Значит, есть путь и без Глитч?"
            Jame "Да. Но он сложнее. Придётся идти наугад, опираясь на эти фрагменты кода. Давайте попробуем."
            window hide
            scene black with dissolve
            pause 1
            scene city with dissolve
            window show
            show jame2_idle with dissolve
            show vanillope at left with dissolve
            show ralph_idle at right with dissolve
            "{i}{alpha=*0.5}Команда идёт по искаженному коридору из переменного кода и красных вспышек, сложнее, чем при помощи Глитч."
            stop music fadeout .5
            Vanillope "Это место кажется странным..."
            Ralph "Здесь ловушки... Осторожнее!"
            play music angry_music fadein .5
            "{i}{alpha=*0.5}Они попадают в ловушку вирусных существ."
            Vanillope "Что нам делать?!"
            window hide
            menu:
                "Атаковать напрямую.":
                    window show
                    Jame "Мы должны проложить себе путь!"
                    Ralph "Согласен! Я прикрою вас!"
                    "{i}{alpha=*0.5}Началось битва. Ребята получили серьезные повреждения, но смогли победить." 
                    Ralph "Нужно было быть осторожнее."
                    Jame "Может, стоило довериться Глитч..."

                "Попытаться обойти.":
                    window show
                    Jame "Может, найдем обходной путь?"
                    Vanillope "Я знаю один! Следуйте за мной!"
                    "{i}{alpha=*0.5}Они обходят опасность, экономя время и ресурсы."
            stop music fadeout 3
            window hide
            scene black with dissolve
            pause 3
            scene city with dissolve
            window show
            play music badass_music fadein 3
            show jame2_idle with dissolve
            show vanillope at left with dissolve
            show ralph_idle at right with dissolve
            Vanillope "Я не уверена, что мы идём правильной дорогой..." 
            Jame "Без Глитч нам сложнее. Но у нас нет выбора. Я анализирую каждую двоичную цепочку, чтобы найти стабильный участок кода..." 
            "{i}{alpha=*0.5}Они продвигаются вперёд, вынуждены несколько раз останавливаться у повторяющихся декораций, но, в конце концов, находят путь к порталу."
            scene portal with dissolve
            show jame2_idle at left with dissolve
            show ralph_idle at right with dissolve
            "{i}{alpha=*0.5}Из портала выходит фигура. Джейм узнает его."
            Jame "Андрей?!"
            show andrey_serious at center with dissolve
            Andrey "Привет, Джейм. Не ожидал тебя здесь увидеть."
            Andrey "Я удивлен, что вы добрались без проводника. Столько усилий впустую!"
            Vanillope "Это тот самый Андрей?"
            "{i}{alpha=*0.5}Ральф кивает, напрягаясь." 
            Jame "Что ты здесь делаешь? Почему ты это делаешь?"
            hide andrey_serious with dissolve
            show andrey_angry with dissolve
            Andrey "Всегда {b}ты{/b} был лучшим. Всегда впереди. Но теперь у меня есть шанс стать первым. С помощью этого вируса я стану властелином этого мира."
            Jame "Это безумие! Ты разрушишь все!"
            hide andrey_angry with dissolve
            show andrey_serious with dissolve
            Andrey "Мне все равно. Я устал быть в тени."
            "{i}{alpha=*0.5}Ральф делает шаг вперед."
            stop music fadeout .5
            play music epic_battle_music fadein .5
            Ralph "Мы не позволим тебе это сделать!"
            "{i}{alpha=*0.5}Начинается битва. Вирусные существа нападают на них. Ральф отбрасывает их мощными ударами, Ванилопа использует свою скорость, чтобы запутать врагов."
            hide ralph_idle with dissolve
            "{i}{alpha=*0.5}Джейм и Андрей стоят друг напротив друга."
            Jame "Пожалуйста, остановись. Это не выход."
            Andrey "Слишком поздно для разговоров."
            "{i}{alpha=*0.5}Они вступают в цифровую схватку. Джейм пытается взломать контроль Андрея над вирусом."
            "{i}{alpha=*0.5}В этот момент начинается мощный сбой. Вирус начинает разрушаться, система перегружается."
            hide andrey_serious with dissolve
            show andrey_angry with dissolve
            Andrey "Нет! Что ты сделал?!"
            "{i}{alpha=*0.5}Портал начинает коллапсировать. Ванилопа и Ральф бегут к выходу."
            show vanillope at right with dissolve
            Vanillope "Джейм! Пора уходить!"
            hide andrey_angry with dissolve
            show andrey_serious with dissolve
            Andrey "Все потеряно..."
            stop music fadeout .5
            window hide
            play music sad_music_2 fadein .5
            menu:
                "Попытаться спасти Андрея":
                    window show
                    $ Friendship_Saves_the_World += 1
                    $ The_Price_of_Mistrustt += 1
                    Jame "Я не оставлю тебя здесь! Давай, уходи со мной!"
                    Andrey "После всего, что я сделал?"
                    Jame "Мы друзья. Вместе мы все исправим."
                    "{i}{alpha=*0.5}Джейм протягивает руку, Андрей принимает ее, и они вместе выбираются."
                    "{i}{alpha=*0.5}Андрей осознает свои ошибки и помогает команде в последние минуты."
                    Andrey "Спасибо... Я поступил ужасно. Помогу вам исправить это."
                    "{i}{alpha=*0.5}Вместе они стабилизируют систему, вирус полностью уничтожен."
                    Vanillope "Рады, что ты с нами."
                    jump epilogue
                
                "Оставить Андрея":
                    window show
                    $ Sacrifice_in_the_Name_of_Salvation += 1
                    $ Lost_Opportunities += 1
                    Jame "Ты сам выбрал этот путь."
                    Andrey "Пожалуйста... Не бросай меня..."
                    Jame "Я не могу рисковать всеми ради тебя."
                    "{i}{alpha=*0.5}Джейм уходит, оставляя Андрея в разрушающемся портале."
                    window hide
                    scene black with dissolve
                    pause .5
                    scene portal with dissolve
                    show vanillope at center with dissolve
                    show ralph_idle at left with dissolve
                    show jame2_sad at right with dissolve
                    Vanillope "Мы могли бы попытаться спасти его..."
                    Ralph "Иногда приходится делать трудный выбор."
                    Jame "Давайте уйдем отсюда."
                    "{i}{alpha=*0.5}Вирус остановлен, но чувство вины остается."
                    jump epilogue


    label epilogue:
        stop music fadeout 3
        play music space_music fadein 3
        window hide
        scene black with dissolve
        pause 3
        if Friendship_Saves_the_World == 3:
            scene wake with dissolve
            window show
            "{i}{alpha=*0.5}Цифровой мир восстановлен, отношения между персонажами крепкие."
            show glitch with dissolve
            show andrey_serious at left with dissolve
            show jame2_idle at right with dissolve
            Glitch "Я нашла свое место благодаря вам." 
            "{i}{alpha=*0.5}Глитч становится файерволом."
            Andrey "Я постараюсь загладить свою вину."
            hide andrey_serious with dissolve
            show vanillope at left with dissolve
            Jame "Я рад, что все закончилось хорошо."
            Vanillope "Ну, теперь пора прощаться?"
            hide vanillope with dissolve
            show ralph_idle at left with dissolve
            Ralph "Спасибо тебе! И удачи!"
            Glitch "Спасибо, будем ждать тебя снова."
            Jame "Спасибо вам за всё, ребята!"
            window hide
            scene wake_light with dissolve
            pause .5
            stop music fadeout 3
            scene black with dissolve
            pause 3
            play music calm_music fadein 3
            scene server with dissolve
            window show
            "{i}{alpha=*0.5}Яркая вспышка. Джейм открывает глаза и обнаруживает себя на полу серверной."
            "{i}{alpha=*0.5}Над ним склонились коллеги."
            Colleague "Джейм! Ты как? Что случилось?"
            show jame_idle with dissolve 
            Jame "Я... Я в порядке. Кажется, перегрузка системы. Нужно проверить оборудование." 
            "Он встает и замечает на экране сообщение: «Вирус устранен. Система восстановлена.»"
            window hide
            scene black with dissolve
            pause 1
            scene park with dissolve
            window show
            "Позже, сидя в парке, Джейм встречается с Андреем."
            show andrey_idle with dissolve
            show jame_idle at left with dissolve
            Andrey "Джейм, я хотел поговорить. Последнее время я чувствовал зависть к тебе. Прости меня."
            Jame "Все в порядке. Я рад, что мы можем обсудить это." 
            "{i}{alpha=*0.5}Они улыбаются друг другу, и напряжение между ними исчезает."
            window hide
            scene black with dissolve
            pause 1
            scene end with dissolve
            window show
            "{i}{alpha=*0.5}Вечером, дома, Джейм садится за компьютер. Экран мерцает, и появляется сообщение:"
            "{i}«Спасибо за помощь! Ждем тебя в гости снова! – Твои друзья из цифрового мира.»"
            "{i}{alpha=*0.5}Джейм улыбается, чувствуя тепло в груди."
            Jame "Я обязательно вернусь."

            window hide
            scene black with dissolve
            pause 2

            return

        if The_Price_of_Mistrustt == 3:
            scene wake with dissolve
            window show
            "{i}{alpha=*0.5}Вирус остановлен, но мир понес большие потери."
            show vanillope with dissolve
            show andrey_serious at left with dissolve
            show jame2_idle at right with dissolve
            Vanillope "Многие исчезли... Глитч тоже."
            Andrey "Я сожалею о том, что натворил."
            Jame "Мы сделали, что могли."
            Vanillope "Видимо, теперь нам пора прощаться?"
            hide andrey_serious with dissolve
            show ralph_idle at left with dissolve
            Ralph "Спасибо, что помог остановить вирус."
            Jame "И вам спасибо, ребята..."
            window hide
            scene wake_light with dissolve
            pause .5
            stop music fadeout 3
            scene black with dissolve
            pause 3
            play music calm_music fadein 3
            scene server with dissolve
            window show
            "{i}{alpha=*0.5}Яркая вспышка. Джейм открывает глаза и обнаруживает себя на полу серверной."
            "{i}{alpha=*0.5}Над ним склонились коллеги."
            Colleague "Джейм! Ты как? Что случилось?"
            show jame_idle with dissolve 
            Jame "Я... Я в порядке. Кажется, перегрузка системы. Нужно проверить оборудование." 
            "Он встает и замечает на экране сообщение: «Вирус устранен. Система восстановлена.»"
            window hide
            scene black with dissolve
            pause 1
            scene park with dissolve
            window show
            "Позже, сидя в парке, Джейм встречается с Андреем."
            show andrey_idle with dissolve
            show jame_idle at left with dissolve
            Andrey "Джейм, я хотел поговорить. Я сожалею о том, что было."
            Jame "Все в порядке." 
            "{i}{alpha=*0.5}Они улыбаются друг другу, но напряжение между ними никуда не уходит."
            window hide
            scene black with dissolve
            pause 1
            scene end with dissolve
            window show
            "{i}{alpha=*0.5}Вечером, дома, Джейм садится за компьютер. Экран мерцает, и появляется сообщение:"
            "{i}«Спасибо за помощь! Ждем тебя в гости снова! – Твои друзья из цифрового мира.»"
            "{i}{alpha=*0.5}Джейм улыбается, чувствуя тепло в груди."
            Jame "Я обязательно вернусь."
            window hide
            scene black with dissolve
            pause 2

            return
        
        if Sacrifice_in_the_Name_of_Salvation == 3:
            scene wake with dissolve
            window show
            "{i}{alpha=*0.5}Мир спасен, но цена высока."
            show glitch at center with dissolve
            show vanillope at left with dissolve
            show jame2_sad at right with dissolve
            Glitch "Ваш выбор спас мир, но потеря болезненна."
            Vanillope "Мы будем помнить его."
            Jame "Я принял трудное решение."
            Vanillope "Видимо, теперь пора прощаться?"
            hide vanillope with dissolve
            show ralph_idle at left with dissolve
            Ralph "Спасибо тебе."
            Glitch "Спасибо, будем ждать тебя снова."
            Jame "Спасибо вам за всё, ребята."
            window hide
            scene wake_light with dissolve
            pause .5
            stop music fadeout 3
            scene black with dissolve
            pause 3
            play music sad_music_1 fadein 3
            scene server with dissolve
            window show
            "{i}{alpha=*0.5}Яркая вспышка. Джейм открывает глаза и обнаруживает себя на полу серверной."
            "{i}{alpha=*0.5}Над ним склонились коллеги."
            Colleague "Джейм! Ты как? Что случилось?"
            show jame_idle with dissolve 
            Jame "Я... Я в порядке. Кажется, перегрузка системы. Нужно проверить оборудование." 
            "Он встает и замечает на экране сообщение: «Вирус устранен. Система восстановлена.»"
            window hide
            scene black with dissolve
            pause 1
            scene park with dissolve
            window show
            "Позже, сидя в парке, Джейм думает обо всём."
            show jame_idle with dissolve
            Jame_thought "Может, не стоило мне его оставлять? Я так сожалею..." 
            "{i}{alpha=*0.5}Джейм сожалеет о своем выборе."
            window hide
            scene black with dissolve
            pause 1
            scene end with dissolve
            window show
            "{i}{alpha=*0.5}Вечером, дома, Джейм садится за компьютер. Экран мерцает, и появляется сообщение:"
            "{i}«Спасибо за помощь! Ждем тебя в гости снова! – Твои друзья из цифрового мира.»"
            "{i}{alpha=*0.5}Джейм улыбается, чувствуя тепло в груди."
            Jame "Я обязательно вернусь."

            return

        if Lost_Opportunities == 3:
            scene wake with dissolve
            window show
            "{i}{alpha=*0.5}Мир частично разрушен, многие персонажи исчезли."
            show vanillope at center with dissolve
            show ralph_idle at left with dissolve
            show jame2_sad at right with dissolve
            Vanillope "Все изменилось... Так много потерь."
            Ralph "Мы выжили, но какой ценой?"
            Jame "Я должен был поступить иначе."
            Vanillope "Ладно, пора прощаться."
            Ralph "Спасибо. Прощай."
            Jame "Прощайте, ребята."
            window hide
            scene wake_light with dissolve
            pause .5
            stop music fadeout 3
            scene black with dissolve
            pause 3
            play music sad_music_2 fadein 3
            scene server with dissolve
            window show
            "{i}{alpha=*0.5}Яркая вспышка. Джейм открывает глаза и обнаруживает себя на полу серверной."
            "{i}{alpha=*0.5}Над ним склонились коллеги."
            Colleague "Джейм! Ты как? Что случилось?"
            show jame_idle with dissolve 
            Jame "Я... Я в порядке. Кажется, перегрузка системы. Нужно проверить оборудование." 
            "Он встает и замечает на экране сообщение: «Вирус устранен. Система восстановлена.»"
            window hide
            scene black with dissolve
            pause 1
            scene park with dissolve
            window show
            "Позже, сидя в парке, Джейм чувствует себя опустошенным."
            show jame_sad with dissolve
            Jame_thought "Столько потерь: Андрей, Глитч...Простите меня" 
            "{i}{alpha=*0.5}Джейму очень тяжело после всего произошедшего."
            window hide
            scene black with dissolve
            pause 1
            scene end with dissolve
            window show
            "{i}{alpha=*0.5}Вечером, дома, Джейм садится за компьютер. Он ожидает каких-то новостей от своих кибер-друзей, но ничего. Экран пустел."
            "{i}{alpha=*0.5}Джейм закрыл лицо руками."
            Jame "Простите, простите..."
            window hide
            scene black with dissolve
            pause 2

            return

        else:
            window hide
            scene black with dissolve
            pause 1
            scene wake with dissolve
            window show
            show vanillope at center with dissolve
            show ralph_idle at left with dissolve
            show jame2_idle at right with dissolve
            Vanillope "Ну, будем прощаться?"
            Ralph "Спасибо тебе! И удачи!"
            Jame "Спасибо вам за всё, ребята!"
            window hide
            scene wake_light with dissolve
            pause .5
            stop music fadeout 3
            scene black with dissolve
            pause 3
            play music calm_music_1 fadein 3
            scene server with dissolve
            window show
            "{i}{alpha=*0.5}Яркая вспышка. Джейм открывает глаза и обнаруживает себя на полу серверной."
            "{i}{alpha=*0.5}Над ним склонились коллеги."
            Colleague "Джейм! Ты как? Что случилось?"
            show jame_sad with dissolve
            Jame "Я... Я в порядке. Кажется, перегрузка системы. Нужно проверить оборудование." 
            "Он встает и замечает на экране сообщение: «Вирус устранен. Система восстановлена.»"
            window hide
            scene black with dissolve
            pause 1
            scene end with dissolve
            window show
            "{i}{alpha=*0.5}Вечером, дома, Джейм садится за компьютер. Экран мерцает, и появляется сообщение:"
            "{i}«Спасибо за помощь! Ждем тебя в гости снова! – Твои друзья из цифрового мира.»"
            "{i}{alpha=*0.5}Джейм улыбается, чувствуя тепло в груди."
            Jame "Я обязательно вернусь."

            window hide
            scene black with dissolve
            pause 2
            
            return
