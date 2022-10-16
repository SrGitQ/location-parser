import React from 'react';
import MBox from '../boxes/MBox';
import { Title } from '../text';
import Place from '../../utils/types';
import Cards from '../organisms/Cards';

type Props = {
	competency: Place[] | null;
}

const TopPlaces: React.FC<Props> = ({competency}) => {
	if (competency && competency.length > 3) {
		competency = competency.slice(0, 3);
	}

	return (
		<div>
			<MBox>
				<Title title='Top Places'/>
				<Cards competency={competency}/>
			</MBox>
		</div>
	);
};

export default TopPlaces;
