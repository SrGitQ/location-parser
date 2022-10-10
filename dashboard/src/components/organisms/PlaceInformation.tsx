import React from 'react';
import { Bullet, GText} from '../text';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { solid } from '@fortawesome/fontawesome-svg-core/import.macro'
import { RBox} from '../boxes';
import Place from '../../utils/types';

type Props = {
	place: Place
}

const PlaceInformation: React.FC <Props> = ({place}) => {
	const image = (<img className='rounded-full h-36 w-36' src={place.img?.src} alt='swipe'/>);
	const information = (
		<div>
			<Bullet>
				<FontAwesomeIcon icon={solid('location-dot')}/> {place.address}
			</Bullet>
			<Bullet>
				<FontAwesomeIcon icon={solid('phone')}/> {place.phone}
			</Bullet>
			<Bullet>
				<FontAwesomeIcon icon={solid('shop')}/> {place.type} <span className={place.status === 'Closed' ? 'text-red-600': 'text-green-600'}>{place.status}</span>
			</Bullet>
		</div>
	);
	
	return (
		<RBox>
			<div className='flex flex-row h-40 my-2'>
				<div className='basis-1/3 grid place-content-center'>
					{image}
				</div>
				<div className='basos-1/2'>
					<GText title={place.name}/>
					{information}
				</div>
			</div>
		</RBox>
	);
};

export default PlaceInformation;