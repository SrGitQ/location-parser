import React from 'react';

type WordCount = {
	text: string;
	value: number;
};

type Sentiment = {
	positive: number;
	neutral: number;
	negative: number;
}


type DayTendency = {
	day: string;
	people: number;
}

type BusyDays = {
	days: DayTendency[];
}

type HourTendency = {
	hour: string;
	people: number;
}
type BusyHours = {
	hours: HourTendency[];
}

type Img = {
	src: string;
}

type Location = {
	lat: number;
	lng: number;
}

type Place = {
	name: string;
	type: string;
	phone: string;
    place_id:string;
	status: string;
    rating: number;
	address: string;
	img: Img | null;
	location: Location;
	ratings_total: number;
	url: string;
	website: string;
	busyDays: BusyDays | null;
	competency: Place[];
	sentiment: Sentiment | null;
	busyHours: BusyHours | null;
	wordCloud: WordCount[] | null;
    reviews: Array<number> | null;
};


export default Place
