import React from 'react'
import MBox from '../boxes/MBox';
import Title from '../text/Title';
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
} from 'chart.js';
import { Scatter } from 'react-chartjs-2';
import Place from '../../utils/types';

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip);

export const options = {
    plugins: {
        tooltip: {
            callbacks: {
                label: function(ctx: any) {
                    // console.log(ctx);
                    let label = ctx.dataset.labels[ctx.dataIndex];
                    label += " (" + ctx.parsed.x + ", " + ctx.parsed.y + ")";
                    return label;
                }
            }
        }
    }
};

type CompetencyPlace = {
	place: Place;
}

const ScoreVsComments: React.FC<CompetencyPlace> = ({place}) => {
	const dots = [
		{y: place.rating, x: place.reviews?.reduce((a, b) => a + b, 0)},
	];
	const labelings = [
		place.name,
	]

	if (place.competency) {

		place.competency.forEach( item => {
			labelings.push(item.name);
			dots.push({y: Number(item.rating), x: item.ratings_total})
		});
	}
	const data = {
		responsive: true,
	  	datasets: [
		{
		  labels: labelings,
		  data: dots,
		  backgroundColor: 'rgb(102,102,102)',
		  
		},
	  ],
	};

	return (
		<MBox>
			<Title title='Score vs Comments'/>
			<div className='mt-[2rem] pl-3 pr-3'>
				<Scatter options={options} data={data} />
			</div>
		</MBox>
	);
};

export default ScoreVsComments;
