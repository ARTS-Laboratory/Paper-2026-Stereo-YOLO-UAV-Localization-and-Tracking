
% Set default font to Times New Roman
set(groot, 'defaultAxesFontName', 'Times New Roman')
set(groot, 'defaultTextFontName', 'Times New Roman')

% Set default font size
set(groot, 'defaultAxesFontSize', 15)
set(groot, 'defaultTextFontSize', 15)

% Optional: Set figure background to white
set(groot, 'defaultFigureColor', 'w')

figure
a1=[1;2;3;4;5;6;7;8;9;10];
x1=[-443.902,-357.549,-367.723,-433.491,-426.555,-386.669,-446.472,-545.982,-587.616,-521.992];
y1=[1099.744,846.4186,547.2737,494.0404,437.3849,290.0504,104.4639,-51.7836,-285.669,-372.941];
z1=[4320.007,4300.523,4206.484,3975.853,3802.073,3699.824,3643.106,3551.769,3495.109,3320.154];

scatter3(x1, y1, z1, 50, 'blue', 'filled');  % size 50, filled circles
hold on;

plot3(x1, y1, z1, '-r', 'LineWidth', 1); %line plot

text(x1,y1,z1,num2str(a1)) 

xlabel('X')
ylabel('Y')
zlabel('Z')
title('OptiTrack 3D plot')


