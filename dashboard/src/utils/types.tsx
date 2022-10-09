import React from 'react';

type Place = {
	name: string;
	address: string;
	phone: string;
	type: string;
	status: string;
    reviews: Array<number>;
    rating: number;
};
export default Place;