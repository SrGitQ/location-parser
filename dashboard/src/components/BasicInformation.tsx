import React from 'react';
import { PlaceInformation, Rating } from './organisms';
import Place from '../utils/types';
import Map from './organisms/Map';
import Map_comp from './organisms/Map_comp'
import Competency from './Competency';

type Props = {
	place: Place;
}

const BasicInformation: React.FC<Props> = ({place}) => {

    let competency = () => {
        if(place.competency){
            return <Map_comp location={place.location} markers={place?.competency?.map(e=>e.location)}/>
        }else {
            return <Map location={place.location}/>
        }
    }

	return (
		<div className='grid grid-cols-2 m-6 gap-6'>
			<div className='grid gap-6'>
				<PlaceInformation place={place}/>
				<Rating reviews={place.reviews} rating={place.rating}/>
			</div>
			<div>
                {competency()}
			</div>
		</div>
	);
};

export default BasicInformation;
