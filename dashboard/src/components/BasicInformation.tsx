import React from 'react';
import { PlaceInformation, Rating } from './organisms';
import Place from '../utils/types';
import Map from './organisms/Map';

type Props = {
	place: Place;
}

const BasicInformation: React.FC<Props> = ({place}) => {
	return (
		<div className='grid grid-cols-2 m-6 gap-6'>
			<div className='grid gap-6'>
				<PlaceInformation place={place}/>
				<Rating reviews={place.reviews} rating={place.rating}/>
			</div>
			<div>
				<Map />
			</div>
		</div>
	);
};

export default BasicInformation;