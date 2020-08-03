import React from 'react';
import {useQuery} from 'react-query';
import axios from 'axios';

const fetchPets = async () => {
    const BASE_URL = 
    process.env.NODE_ENV !== 'production' ? 
    'http://localhost:8000' : 
    'http://www.baytownhumanesociety.org/';

    const {data} = await axios.get(new URL(`${BASE_URL}/pets`));
    console.log(data.pets)
    return data.pets;
}

const Pets = () => {
const { data, status } = useQuery('petsQ', fetchPets);
return(
        <>
        <p>PETS {status !== 'success' ? status : null}</p>
            {
                status === 'success' && (
                    data.map((pet) => {
                        return (
                            <h1>{pet.animal_name}</h1>
                        )
                    })
                )
            }
        </>
    )
}

export default Pets;