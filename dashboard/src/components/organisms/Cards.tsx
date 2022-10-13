import React from 'react';
import Place from '../../utils/types';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { solid } from '@fortawesome/fontawesome-svg-core/import.macro'

type BulletsProps = {
    place: Place;
}

const BulletPlaceInformtion: React.FC <BulletsProps> = ({place}) => {
	const image = (<img className='rounded-full h-16 w-16' src='https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279' alt='swipe'/>);
	const information = (
		<div className=''>
            <div className='text-neutral-400 text-[0.8rem]'>
				<FontAwesomeIcon icon={solid('location-dot')}/> {place.address.slice(0,15)}...
            </div>
            <div className='text-neutral-400 text-[0.8rem]'>
				<FontAwesomeIcon icon={solid('phone')}/> {place.phone}
            </div>
            <div className='text-neutral-400 text-[0.8rem]'>
				<FontAwesomeIcon icon={solid('shop')}/> {place.type} <span className={place.status === 'Closed' ? 'text-red-600': 'text-green-600'}>{place.status}  </span>
            </div>
		</div>
	);
	
	return (
		<div className='flex flex-row h-32 w-[280px]'>
			<div className='basis-1/3 grid place-content-center'>
				{image}
			</div>
			<div className='basis-2/3'>
				{place.name}  {place.rating}⭑
				{information}
                
			</div>
		</div>
	);
};

type CardInfo = {
    place: Place;
}

const Card: React.FC <CardInfo> = ({place}) => {
    return (
        <div className='h-[160px] bg-zinc-200 w-[300px] p-1 rounded-lg'>
            <a href={'http://localhost:5000/place/'+place.place_id}><BulletPlaceInformtion place={place}/></a>
        </div>
    );
};

type CardsComp = {
    competency: Place[] | null;
}

const Cards: React.FC <CardsComp> = ({competency}) => {
    const layout = (
        <div className='grid grid-cols-4 gap-3 m-4 h-[4rem]'>
            {competency?.map((place, index) => (
                <Card place={place} key={index}/>
            ))}
        </div>
    )

    return (<>{layout}</>);
};

export default Cards;
