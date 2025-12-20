function [x_new, y_new, z_new] = transformCoordinates(x, y, z, rotation_deg, translation)
    %TRANSFORMCOORDINATES Rotates and translates 3D coordinates.
    %
    %   [x_new, y_new, z_new] = transformCoordinates(x, y, z, rotation_deg, translation)
    %
    %   Inputs:
    %       x, y, z         - Vectors of original 3D coordinates
    %       rotation_deg    - [rx, ry, rz] rotation angles in degrees (around X, Y, Z axes)
    %       translation     - [tx, ty, tz] translation vector
    %
    %   Outputs:
    %       x_new, y_new, z_new - Transformed coordinates

    % Convert degrees to radians
    rx = deg2rad(rotation_deg(1));
    ry = deg2rad(rotation_deg(2));
    rz = deg2rad(rotation_deg(3));

    % Rotation matrices
    Rx = [1, 0, 0;
          0, cos(rx), -sin(rx);
          0, sin(rx), cos(rx)];

    Ry = [cos(ry), 0, sin(ry);
          0, 1, 0;
         -sin(ry), 0, cos(ry)];

    Rz = [cos(rz), -sin(rz), 0;
          sin(rz), cos(rz), 0;
          0, 0, 1];

    % Combined rotation matrix: R = Rz * Ry * Rx
    R = Rz * Ry * Rx;

    % Apply rotation and translation
    coords = [x(:)'; y(:)'; z(:)'];  % Make sure input is 3xN
    transformed = R * coords + translation(:);

    % Extract output
    x_new = transformed(1, :)';
    y_new = transformed(2, :)';
    z_new = transformed(3, :)';
end
