import React from 'react';
import { MBox } from './boxes';
import { Title} from './text';
import { PlaceInformation, Rating } from './organisms';
import Place from '../utils/types';

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
			<MBox>
				<Title title='Route'/>
			</MBox>
		</div>
	);
};

export default BasicInformation;