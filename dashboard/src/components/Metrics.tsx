import React from 'react';
import { RBox, MBox } from './boxes';

const Metrics: React.FC = () => {
  return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<MBox>
				Words Cloud
			</MBox>
			<div className='grid gap-6'>
				<RBox>
					Opinions
				</RBox>
				<RBox>
					QR
				</RBox>
			</div>
		</div>
  );
};

export default Metrics;