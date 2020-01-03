function verifyBirthday(year, month, day, birthday) {
    var now = new Date();
    var nowYear = now.getFullYear();
    //年月日是否合理
    if (birthday.getFullYear() === year && (birthday.getMonth() + 1) === month && birthday.getDate() === day) {
        //判断年份的范围（3岁到100岁之间)
        var time = nowYear - year;
        if (time >= 3 && time <= 150) {
            return true;
        }
        return false;
    }
    return false;
}
