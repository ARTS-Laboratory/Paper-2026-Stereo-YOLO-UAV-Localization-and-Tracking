
% Set default font to Times New Roman
set(groot, 'defaultAxesFontName', 'Times New Roman')
set(groot, 'defaultTextFontName', 'Times New Roman')

% Set default font size
set(groot, 'defaultAxesFontSize', 15)
set(groot, 'defaultTextFontSize', 15)

% Optional: Set figure background to white
set(groot, 'defaultFigureColor', 'w')


a1=[1;2;3;4;5;6;7;8;9;10];
x1=[1850,1862,1774,1701,1658,1635,1581,1555,1532,1001];
y1=[1369.5,1306,1199.5,1175,1149.5,1083,987.5,900,768.5,667.5];
z1=[2129,2083,2074,2029,1976,1928,1937,1933,1884,1788];


% Transformation
rotation_deg =  [0, -50, 0];
translation =   [0, 0, 0];

% Call the function
[x_t, y_t, z_t] = transformCoordinates(x1, y1, z1, rotation_deg, translation);

% Plot
figure
scatter3(x_t, y_t, z_t, 50, 'blue', 'filled');
hold on;
plot3(x_t, y_t, z_t, '-r', 'LineWidth', 2);
text(x_t, y_t, z_t, num2str(a1));

xlabel('X')
ylabel('Y')
zlabel('Z')
title('FLIR Manually marked 3D Plot')
