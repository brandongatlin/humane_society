import React from 'react';
import { useQuery } from 'react-query';
import axios from 'axios';
import PetCard from '../PetCard';

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
                <div className='pet-grid'>
                {data.map((pet) => {
                    return (
                      <PetCard animalName={pet.animal_name} src={`${MEDIA_URL}/${pet.image}`} description={pet.description} birth={pet.birth_date}/>
                    )
                })}
                </div>
            )
        }
    </>
    )
}

export default Pets;