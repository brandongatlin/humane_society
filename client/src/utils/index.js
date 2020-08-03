const BASE_URL =
    process.env.NODE_ENV !== 'production' ?
    'http://localhost:8000' :
    'http://www.baytownhumanesociety.org/';

const MEDIA_URL = `${BASE_URL}/media`;

const formatBirthday = (date) => {
    // 2016-11-02T03:50:00Z
    const dif = new Date() - new Date(date);
    const days = Math.floor(dif / 1000 / 86400);
    const years = Math.floor(days / 365);
    const months = Math.floor((days) % 365 / 30);
    const weeks = Math.floor(days / 7);

    const hasAnS = (num) => {
        if (num < 2) {
            return false;
        }
        return true;
    }

    const addS = (str) => {
        return str += 's';
    }

    let formattedTime = '';
    if (years > 0) {
        formattedTime += `${years} ${hasAnS(years) ? addS('Year') : 'Year'}`;
    }

    if (years > 0 && months > 0) {
        formattedTime += ' & ';
    }

    if (months > 0 && months < 12) {
        formattedTime += `${months} ${hasAnS(months) ? addS('Month') : 'Month'}`;
    }

    if (years === 0 && months === 0 && weeks === 0) {
        formattedTime += `${days} ${hasAnS(days) ? addS('Day') : 'Day'}`;
    } else if (years === 0 && months === 0) {
        formattedTime += `${weeks} ${hasAnS(weeks) ? addS('Week') : 'Week'}`;
    }

    return formattedTime + ' Old';
}


export { BASE_URL, MEDIA_URL, formatBirthday };