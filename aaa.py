import datetime
import shuijishu
import card2
import time


def sd():
    year = datetime.datetime.today().year

    year = str(year)
    with open(file="gudingjie.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + "固定纪念日" + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:" + year + "固定纪念日\n"
        file_object.write(start_string)

        body_string = ("BEGIN:VEVENT\nDTSTAMP:20190912T184136Z\nUID:",
                       "END:VEVENT\n")

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0214" + "\nDTEND;VALUE=DATE:" + year + "0214" + "\n"
        beizhu = "DESCRIPTION:" + '214情人节' + "\n"
        body3 = "SUMMARY:" + "214" + '' + "情人节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0214T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0520" + "\nDTEND;VALUE=DATE:" + year + "0520" + "\n"
        beizhu = "DESCRIPTION:" + '520网络情人节' + "\n"
        body3 = "SUMMARY:" + "214" + '' + "520网络情人节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0520T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0308" + "\nDTEND;VALUE=DATE:" + year + "0308" + "\n"
        beizhu = "DESCRIPTION:" + '38妇女节' + "\n"
        body3 = "SUMMARY:" + "38" + '' + "妇女节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0308T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0312" + "\nDTEND;VALUE=DATE:" + year + "0312" + "\n"
        beizhu = "DESCRIPTION:" + '312植树节' + "\n"
        body3 = "SUMMARY:" + "312" + '' + "植树节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0312T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0315" + "\nDTEND;VALUE=DATE:" + year + "0315" + "\n"
        beizhu = "DESCRIPTION:" + '315消费者日' + "\n"
        body3 = "SUMMARY:" + "315消费者日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0315T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0422" + "\nDTEND;VALUE=DATE:" + year + "0422" + "\n"
        beizhu = "DESCRIPTION:" + '422地球日' + "\n"
        body3 = "SUMMARY:" + "422地球日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0422T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0504" + "\nDTEND;VALUE=DATE:" + year + "0504" + "\n"
        beizhu = "DESCRIPTION:" + '青年节' + "\n"
        body3 = "SUMMARY:" + "青年节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0504T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0512" + "\nDTEND;VALUE=DATE:" + year + "0512" + "\n"
        beizhu = "DESCRIPTION:" + '512全国防灾减灾日、护士节' + "\n"
        body3 = "SUMMARY:" + "512全国防灾减灾日、护士节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0512T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0605" + "\nDTEND;VALUE=DATE:" + year + "0605" + "\n"
        beizhu = "DESCRIPTION:" + '世界环境日' + "\n"
        body3 = "SUMMARY:" + "世界环境日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0605T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0701" + "\nDTEND;VALUE=DATE:" + year + "0701" + "\n"
        beizhu = "DESCRIPTION:" + '七一建党节（1921-07-01）、香港回归日' + "\n"
        body3 = "SUMMARY:" + "七一建党节;香港回归日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0701T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0801" + "\nDTEND;VALUE=DATE:" + year + "0801" + "\n"
        beizhu = "DESCRIPTION:" + '八一建军节' + "\n"
        body3 = "SUMMARY:" + "八一建军节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0801T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0815" + "\nDTEND;VALUE=DATE:" + year + "0815" + "\n"
        beizhu = "DESCRIPTION:" + '日本投降(Japanese surrender)是指1945年8月15日正午，日本天皇向全日本广播，接受波茨坦公告、实行无条件投降，结束战争。1945年8月21日今井武夫飞抵芷江洽降。1945年9月2日上午9时，标志着第二次世界大战结束的日本投降的签字仪式，在停泊在东京湾的密苏里号主甲板上举行。日本外相重光葵代表日本天皇和政府、陆军参谋长梅津美治郎代表日军大本营在投降书上签字。1945年9月9日上午，中国战区受降仪式在中国南京中央军校大礼堂举行。1945年10月25日，中国国民政府在台湾举行受降仪式，这成为抗日战争取得完全胜利的重要标志。' + "\n"
        body3 = "SUMMARY:" + "日本投降日（1945-08-15）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0815T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0910" + "\nDTEND;VALUE=DATE:" + year + "0910" + "\n"
        beizhu = "DESCRIPTION:" + '910教师节' + "\n"
        body3 = "SUMMARY:" + "910教师节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0910T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0903" + "\nDTEND;VALUE=DATE:" + year + "0903" + "\n"
        beizhu = "DESCRIPTION:" + '1945年9月2日，日本向盟军投降仪式在东京湾密苏里号军舰上举行。在包括中国在内的9个受降国代表注视下，日本在投降书上签字。这是中国近代以来反侵略历史上的第一次全面胜利，也为世界反法西斯战争的胜利做出了巨大贡献。之后每年的9月3日，被确定为中国人民抗日战争胜利纪念日' + "\n"
        body3 = "SUMMARY:" + "抗战胜利日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0903T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0707" + "\nDTEND;VALUE=DATE:" + year + "0707" + "\n"
        beizhu = "DESCRIPTION:" + '1937年7月7日夜，卢沟桥的日本驻军在未通知中国地方当局的情况下，径自在中国驻军阵地附近举行所谓军事演习，并诡称有一名日军士兵失踪，要求进入北平西南的宛平县城（今卢沟桥镇）搜查，被中国驻军严词拒绝，日军随即向宛平城和卢沟桥发动进攻。中国驻军第29军37师219团奋起还击，进行了顽强的抵抗。“七七事变”揭开了全国抗日战争的序幕 ' + "\n"
        body3 = "SUMMARY:" + "七七事变（中华民族全面抗战的起点）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0707T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1010" + "\nDTEND;VALUE=DATE:" + year + "1010" + "\n"
        beizhu = "DESCRIPTION:" + '辛亥革命（1911-10-10）;大会员萌节' + "\n"
        body3 = "SUMMARY:" + "辛亥革命;大会员萌节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1010T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1213" + "\nDTEND;VALUE=DATE:" + year + "1213" + "\n"
        beizhu = "DESCRIPTION:" + '南京大屠杀死难者国家公祭日是中国政府设立的纪念日，以国家公祭的方式，祭奠在南京大屠杀中死亡的30多万同胞。2014年2月27日，十二届全国人大常委会第七次会议通过决定，以立法形式将12月13日设立为南京大屠杀死难者国家公祭日。 决议的通过，使得对南京大屠杀遇难者的纪念上升为国家层面， 表明了中国人民反对侵略战争、捍卫人类尊严、维护世界和平的坚定立场。' + "\n"
        body3 = "SUMMARY:" + "南京大屠杀死难者国家公祭日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1213T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1220" + "\nDTEND;VALUE=DATE:" + year + "1220" + "\n"
        beizhu = "DESCRIPTION:" + '澳门回归（1999-12-20）' + "\n"
        body3 = "SUMMARY:" + "澳门回归" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1220T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0406" + "\nDTEND;VALUE=DATE:" + year + "0406" + "\n"
        beizhu = "DESCRIPTION:" + '小米米粉节' + "\n"
        body3 = "SUMMARY:" + "小米米粉节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0406T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0816" + "\nDTEND;VALUE=DATE:" + year + "0816" + "\n"
        beizhu = "DESCRIPTION:" + '小米816节' + "\n"
        body3 = "SUMMARY:" + "小米816节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0816T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1024" + "\nDTEND;VALUE=DATE:" + year + "1024" + "\n"
        beizhu = "DESCRIPTION:" + '1024程序员节' + "\n"
        body3 = "SUMMARY:" + "1024程序员节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1024T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0626" + "\nDTEND;VALUE=DATE:" + year + "0626" + "\n"
        beizhu = "DESCRIPTION:" + 'B站周年庆' + "\n"
        body3 = "SUMMARY:" + "B站周年庆" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0626T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0519" + "\nDTEND;VALUE=DATE:" + year + "0519" + "\n"
        beizhu = "DESCRIPTION:" + '中国旅游日' + "\n"
        body3 = "SUMMARY:" + "中国旅游日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0519T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0808" + "\nDTEND;VALUE=DATE:" + year + "0808" + "\n"
        beizhu = "DESCRIPTION:" + '全民健身日;2008北京奥运会' + "\n"
        body3 = "SUMMARY:" + "全民健身日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0808T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0918" + "\nDTEND;VALUE=DATE:" + year + "0918" + "\n"
        beizhu = "DESCRIPTION:" + '九·一八事变，又称奉天事变、柳条湖事件。是1931年9月18日日本驻中国东北地区的关东军突然袭击沈阳，以武力侵占东北的事件。九·一八事变是由日本蓄意制造并发动的侵华战争，是日本帝国主义企图以武力征服中国的开端，是中国抗日战争的起点，标志着中国局部抗战的开始，揭开了第二次世界大战东方战场的序幕。九一八事变后，中国人民的局部抗战也标志着世界反法西斯战争的起点。' + "\n"
        body3 = "SUMMARY:" + "九·一八纪念日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0918T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1201" + "\nDTEND;VALUE=DATE:" + year + "1201" + "\n"
        beizhu = "DESCRIPTION:" + '世界艾滋病日' + "\n"
        body3 = "SUMMARY:" + "世界艾滋病日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1201T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "0618" + "\nDTEND;VALUE=DATE:" + year + "0618" + "\n"
        beizhu = "DESCRIPTION:" + '京东618购物节' + "\n"
        body3 = "SUMMARY:" + "京东618购物节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "0618T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1111" + "\nDTEND;VALUE=DATE:" + year + "1111" + "\n"
        beizhu = "DESCRIPTION:" + '双11' + "\n"
        body3 = "SUMMARY:" + "双11" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1111T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        body2 = "DTSTART;VALUE=DATE:" + year + "1212" + "\nDTEND;VALUE=DATE:" + year + "1212" + "\n"
        beizhu = "DESCRIPTION:" + '双12' + "\n"
        body3 = "SUMMARY:" + "双12" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + "1212T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.chuyi()
        time.sleep(7)

        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '大年初一(春节)' + "\n"
        body3 = "SUMMARY:" + "大年初一(春节)" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk+"T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.yuanxiao()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '正月十五(元宵节)' + "\n"
        body3 = "SUMMARY:" + "正月十五(元宵节)" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.duanwu()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '端午节（农历五月初五）' + "\n"
        body3 = "SUMMARY:" + "端午节（农历五月初五）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + card2.duanwu() + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.qixi()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk+ "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '七夕节（农历七月初七）' + "\n"
        body3 = "SUMMARY:" + "七夕节（农历七月初七）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.zhongyuan1()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '中元节（七月半）今天开始' + "\n"
        body3 = "SUMMARY:" + "中元节（七月半）今天开始" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.zhongyuan2()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '中元节（七月半）今天结束' + "\n"
        body3 = "SUMMARY:" + "中元节（七月半）今天结束" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.zhongqiu()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '中秋节（农历八月十五）' + "\n"
        body3 = "SUMMARY:" + "中秋节（农历八月十五）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.chongyang()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '重阳节（农历九月九）' + "\n"
        body3 = "SUMMARY:" + "重阳节（农历九月九）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.laba()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '腊八节（农历十二月初八）' + "\n"
        body3 = "SUMMARY:" + "腊八节（农历十二月初八）" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.xiaonian1()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '小年（北方），灶王节，扫尘日' + "\n"
        body3 = "SUMMARY:" + "小年（北方），灶王节，扫尘日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.xiaonian2()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '小年（南方），灶王节，扫尘日' + "\n"
        body3 = "SUMMARY:" + "小年（南方），灶王节，扫尘日" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.qingming1()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '清明节(今天开始)' + "\n"
        body3 = "SUMMARY:" + "清明节(今天开始)" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.qingming2()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '清明节' + "\n"
        body3 = "SUMMARY:" + "清明节" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)

        body0 = body_string[0]
        body1 = year + 'almanac_in_' + shuijishu.suiji() + "\n"
        djk=card2.qingming3()
        time.sleep(7)
        body2 = "DTSTART;VALUE=DATE:" + year + djk + "\nDTEND;VALUE=DATE:" + year + djk + "\n"
        beizhu = "DESCRIPTION:" + '清明节(结束日)' + "\n"
        body3 = "SUMMARY:" + "清明节(结束日)" + "\n"
        tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + year + djk + "T-20000Z" + "\n"
        tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
        body4 = body_string[1]
        full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
        file_object.write(full_body)



        end_string = "END:VCALENDAR"
        file_object.write(end_string)






if __name__ == '__main__':
    a = sd()
    print(a)
