import React from 'react';
import {
  Card, CardText, CardBody, CardLink,
  CardTitle, CardSubtitle
} from 'reactstrap';

import { formatBirthday } from '../../utils';

const PetCard = ({animalName, src, description, birth}) => {

  return (
      <Card>
        <CardBody>
          <CardTitle>{animalName}</CardTitle>
          <CardSubtitle>{formatBirthday(birth)}</CardSubtitle>
        </CardBody>
        <img className="petImg" src={src} alt="Card image cap" />
        <CardBody>
          <CardText>{description}</CardText>
          {/* <CardLink href="#">Card Link</CardLink>
          <CardLink href="#">Another Link</CardLink> */}
        </CardBody>
      </Card>
  );
};

export default PetCard;