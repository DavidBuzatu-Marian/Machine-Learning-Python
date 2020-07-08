function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    h = X * theta;
    partSum = [0; 0];
    for i = 1: m
        partSum(1) = partSum(1) + (h(i) - y(i)) * X(i, 1);
        partSum(2) = partSum(2) + (h(i) - y(i)) * X(i, 2);
    end
    tempTheta1 = theta(1) - (alpha / m) * partSum(1);
    tempTheta2 = theta(2) - (alpha / m) * partSum(2);
    % OR %
    %
    % tempTheta1 = theta(1) - (alpha / m) * sum((h - y) .* X(:, 1));
    % tempTheta2 = theta(2) - (alpha / m) * sum((h - y) .* X(:, 2));
    %
    theta = [tempTheta1; tempTheta2];





    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

end
