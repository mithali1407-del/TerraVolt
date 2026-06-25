hours = 0:23;

demand = [

40 35 30 28 25 35 ...
60 80 95 110 125 140 ...
150 145 135 120 100 90 ...
85 75 65 55 50 45

];


plot(hours,demand)


grid on


xlabel('Hours')


ylabel('Demand (kWh)')


title('Community Demand Pattern')