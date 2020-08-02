import React from 'react';
import {useQuery} from 'react-query';
import axios from 'axios';

const fetchPets = async () => {
    const BASE_URL = process.env.NODE_ENV !== 'production' ? 'http://localhost:8000' : 'http://www.baytownhumanesociety.org/';
    const res = await axios.get(`${BASE_URL}/pets`);
    console.log(res);
    return res;
}

const Pets = () => {
    const { pets, status } = useQuery('pets', fetchPets);
    return(
        <h1>PETS {status !== 'success' ? status : null}</h1>
    )
}

export default Pets;