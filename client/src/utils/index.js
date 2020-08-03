const BASE_URL =
    process.env.NODE_ENV !== 'production' ?
    'http://localhost:8000' :
    'http://www.baytownhumanesociety.org/';

const MEDIA_URL = `${BASE_URL}/media`;

export { BASE_URL, MEDIA_URL };