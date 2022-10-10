import React from 'react';
import { LBox } from './boxes';
import { Cards } from './organisms';
import { Title } from './text';
const Competency: React.FC = () => {
	return (
		<LBox>
			<Title title='Competency'/>
			<Cards />
		</LBox>
	);
};

export default Competency;