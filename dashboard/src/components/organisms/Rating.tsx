import React from 'react';
import { RBox } from '../boxes';
import { GText, Title as Tg } from '../text';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { solid } from '@fortawesome/fontawesome-svg-core/import.macro'

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
);

export const options = {
    indexAxis: 'y' as const,
    responsive: true,
    scales: {
        x: {
            grid: {
                display: false,
            },
            ticks: {
                display: false,
            },
            stacked: true,
        },
        y: {
            grid: {
                display: false,
            },
            stacked: true,
        },
    },
    maintainAspectRatio: false
};


type Props = {
    reviews: Array<number> | null;
    rating: number;
}
type Solo = {
    reviews: Array<number> | null;
}

const Chart: React.FC <Solo> = ({reviews}) => {
    const percentageParser = (data: Array<number>) => {
        let total = data.reduce((a, b) => a + b, 0);
        let percentage = data.map((item) => {
            return (item / total);
        });
        return percentage;
    }

    const labels = ['5', '4', '3', '2', '1'];
    let porc = percentageParser(reviews ? reviews : [0, 0, 0, 0, 0]);

    const data = {
        labels,
        datasets: [
          {
            data: porc,
            backgroundColor: 'rgb(255,193,8)',
            borderRadius: 10,
          },
          {
            data: porc.map((item) => {
                return 1 - item;
            }),
            backgroundColor: 'rgb(232, 232, 232 )',
            borderRadius: 10,
          },
        ],
    };

    return <Bar options={options} data={data} />
};

const Rating: React.FC <Props> = ({reviews, rating}) => {

    return (
        <RBox>
            <Tg title='Rating'/>
            <div className='flex'>
                <div className='w-3/4'>
                    <Chart reviews={reviews}/>
                </div>
                <div className='grid content-end w-1/5 ml-2 my-2 pl-5 pb-5'>
                    <div className='grid grid-cols-2 gap-2'>
                        <GText title={rating.toString()}/>
                        <FontAwesomeIcon icon={solid('star')} className='ml-6 mt-2 text-2xl text-amber-400'/>
                    </div>
                    <div className='text-neutral-400 text-sm'>{reviews?.reduce((a,b)=>a+b,0)} Reviews</div>
                </div>
            </div>
        </RBox>
    );
}

export default Rating;
