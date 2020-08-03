import React from 'react';
import { useQuery } from 'react-query';
import axios from 'axios';

import { BASE_URL, MEDIA_URL } from '../../utils';

const fetchPets = async () => {
    const { data } = await axios.get(new URL(`${BASE_URL}/pets`));
    console.log(data.pets)
    return data.pets;
}

const Pets = () => {
const { data, status } = useQuery('petsQuery', fetchPets);

return(
    <>
    <p>{status !== 'success' ? status : null}</p>
        {
            status === 'success' && (
                data.map((pet) => {
                    return (
                    <p>{pet.animal_name}</p>
                        // <img alt={`${pet.animal_name} ${pet.description}`} src={`${MEDIA_URL}/${pet.image}`}/>
                    )
                })
            )
        }
    </>
    )
}

export default Pets;