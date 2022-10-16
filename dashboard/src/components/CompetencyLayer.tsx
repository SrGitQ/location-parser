import React from 'react'
import Place from '../utils/types';
import ScoreVsComments from './organisms/SvsC'
import TopPlaces from './organisms/TopPlaces'

type CompetencyPlace = {
	place: Place;
}

const CompetencyLayer: React.FC<CompetencyPlace> = ({ place }) => {
	return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<TopPlaces competency={place.competency}/>
			<ScoreVsComments place={place}/>
		</div>
	);
};

export default CompetencyLayer;
