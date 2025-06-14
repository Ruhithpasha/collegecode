{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "980c13f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00        36\n",
      "           1       0.95      0.97      0.96        36\n",
      "           2       1.00      1.00      1.00        35\n",
      "           3       1.00      1.00      1.00        37\n",
      "           4       0.97      1.00      0.99        36\n",
      "           5       1.00      1.00      1.00        37\n",
      "           6       1.00      1.00      1.00        36\n",
      "           7       0.97      1.00      0.99        36\n",
      "           8       1.00      0.94      0.97        35\n",
      "           9       1.00      0.97      0.99        36\n",
      "\n",
      "    accuracy                           0.99       360\n",
      "   macro avg       0.99      0.99      0.99       360\n",
      "weighted avg       0.99      0.99      0.99       360\n",
      "\n",
      "Confusion Matrix:\n",
      " [[36  0  0  0  0  0  0  0  0  0]\n",
      " [ 0 35  0  0  1  0  0  0  0  0]\n",
      " [ 0  0 35  0  0  0  0  0  0  0]\n",
      " [ 0  0  0 37  0  0  0  0  0  0]\n",
      " [ 0  0  0  0 36  0  0  0  0  0]\n",
      " [ 0  0  0  0  0 37  0  0  0  0]\n",
      " [ 0  0  0  0  0  0 36  0  0  0]\n",
      " [ 0  0  0  0  0  0  0 36  0  0]\n",
      " [ 0  2  0  0  0  0  0  0 33  0]\n",
      " [ 0  0  0  0  0  0  0  1  0 35]]\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA34AAAGGCAYAAAAkd1NJAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy88F64QAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAe1klEQVR4nO3dbWyd9Xk/8MuN04xQkyMlaQLJiKswKRENnDQtZaVVzHhqgcWhWlk00topoZGGpialixB0izfQ0qlMc1spysSDHZgHhSEZ1IruxYhDKpXyVCNSVdqY4ozSgoDVLGLdYif3/0X/uDUhtAk/OD6XPx/pvMjtc3/P77Z8nft8c/sct1RVVQUAAABpvafRCwAAAOCdpfgBAAAkp/gBAAAkp/gBAAAkp/gBAAAkp/gBAAAkp/gBAAAkp/gBAAAkp/gBAAAkN+2KX39/f7S0tEzcWltbY/HixbFhw4Z4/vnn35U1tLe3R3d39wntOzIyMmn9v3675557yi4UppBmn90nn3wyrr322lixYkW0tbXFggUL4sILL4yHH3647CJhimn22Y2IePbZZ+Ozn/1snH766XHSSSfF0qVL40tf+lK88sor5RYJU1CG+f3KV74Sl19+eSxatChaWlreVlaza230Ahqlr68vli1bFr/4xS/ikUceie3bt8eePXvimWeeiZNPPrnRy/uN/uzP/iz+5E/+ZNK23/u932vQauDd06yze/fdd8djjz0Wn//85+Pss8+O1157LXbu3BkXXHBB7Nq1Kz73uc81eonwjmrW2X3ppZfi3HPPjVNOOSVuuummOP300+OHP/xhbNu2LXbv3h1PPvlkvOc90+7/0ZlmmnV+IyL+/u//Ps4666xYs2ZN3HHHHY1eTkNN2+L3wQ9+MD784Q9HRMT5558fhw8fjptuuikGBwfjqquuetN9/ud//idmz579bi7zmE4//fQ499xzG70MeNc16+xu3bo1brnllknbLr300vjQhz4Uf/3Xf634kV6zzu4DDzwQr7zySnzrW9+KCy64ICJ+uf7/+7//ixtuuCGefvrpWLlyZUPXCO+0Zp3fiIiDBw9O/OfMXXfd1eDVNJb/ovr/Xi9RBw4ciIiI7u7ueN/73hfPPPNMXHzxxdHW1jbxhH/o0KG4+eabY9myZTFr1qyYP39+bNiwIV566aVJmWNjY7F169ZYuHBhzJ49Oz7+8Y/HY4899u4eGCTXLLP7/ve//6htM2bMiFWrVsVzzz33trKhGTXL7M6cOTMiIubMmTNpe61Wi4iI3/md33lb+dCMmmV+I8IV+V8zba/4vdGzzz4bERHz58+f2Hbo0KFYs2ZNbNq0Ka6//voYHx+PI0eORGdnZ+zduze2bt0aH/vYx+LAgQOxbdu26OjoiCeeeCJOOumkiIi45ppr4s4774wvf/nLcdFFF8W+ffvi05/+dBw8ePCox29vb4+IX76H77fx1a9+NW644YZobW2ND33oQ7F169ZYs2bN2/smQBNqttn9dePj47F3794488wzj//Aock1y+yuXbs2Tj/99Ljuuutix44dsWTJknjqqafiq1/9avzhH/5hLF++vMw3BJpIs8wvb1BNM319fVVEVI8++mg1NjZWHTx4sPr2t79dzZ8/v2pra6teeOGFqqqqqqurq4qI6o477pi0/913311FRHX//fdP2v74449XEVHt2LGjqqqq+vGPf1xFRLVly5ZJ9xsYGKgiourq6pq0fenSpdXSpUt/4/p/+tOfVtdcc0117733Vnv37q0GBgaqc889t4qI6tZbbz3ebwc0jWaf3Tdz4403VhFRDQ4OntD+0AwyzO5Pf/rT6vd///eriJi4feYzn6n+93//93i+FdB0Mszvrzv55JOPyppOpm3xe+NtxYoV1fe+972J+73+A/zqq69O2v+qq66qarVadejQoWpsbGzSbeHChdWVV15ZVVVV7dixo4qI6oknnpi0/9jYWNXa2lr0h+7QoUPVypUrq7lz51ZjY2PFcmEqyTa7t956axUR1XXXXVckD6aqZp/d//qv/6o+8pGPVGeeeWY1MDBQPfLII9WOHTuqU089tbr44oudd0mt2ef3jaZ78Zu2v+p55513xvLly6O1tTUWLFgQp5566lH3mT17dpxyyimTtr344osxOjoa733ve9809+WXX46ImPiI54ULF076emtra8ydO7fEIUyYOXNm/PEf/3Fcf/318e///u9+7YTUMsxuX19fbNq0Kb7whS/E1772tSKZMNU16+z+7d/+bQwPD8eBAwcm1vyJT3wili1bFn/wB38QAwMD0dXVdcL50AyadX6ZbNoWv+XLl098OtGxtLS0HLVt3rx5MXfu3Pjud7/7pvu0tbVFREz8kL7wwguxaNGiia+Pj4+/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4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJCc4gcAAJBcS1VVVSMeeGhoqFjWyMhIsayIiM2bNxfNGx4eLppX8njr9XqxrIiIWq1WNI/cOjo6Gr2Et9Tb21s0r6enp1hWe3t7sayI8sfK1FPyvHv++ecXy4qI2L9/f9G80q8LSs6H2aWRSj4PRJR/Lti2bVvRvJK6u7uL5pV+LvhtuOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQnOIHAACQXEtVVVWjF/F29ff3F80bHR0tmrd58+aieZBFS0tLo5fQtPr6+ormdXd3F81j6il5buvo6CiWFRHR3t5eNK9erxfNGxoaKppX0lReG1NP6dnds2dP0byprLOzs2je4OBg0bzfhit+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAySl+AAAAybU2egElDA0NFc3r7u4umge8uSVLlhTNGx0dLZpXr9eL5m3ZsqVYVmdnZ7EspodarVYsq/R5d+3atUXz/uqv/qpoXsnnqv7+/mJZTA8jIyPFsoaHh4tlRUScffbZRfM2b95cNK+9vb1YVunXBI3gih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByih8AAEByLVVVVY1eBAAAAO8cV/wAAACSU/wAAACSU/wAAACSU/wAAACSU/wAAACSU/wAAACSU/wAAACSU/wAAACSU/wAAACS+38jnKfuRg7g+gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1000x400 with 8 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import required libraries\n",
    "from sklearn import datasets\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load MNIST digits dataset\n",
    "digits = datasets.load_digits()\n",
    "\n",
    "# Features and labels\n",
    "X = digits.data\n",
    "y = digits.target\n",
    "\n",
    "# Split into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42, stratify=y\n",
    ")\n",
    "\n",
    "# Feature scaling\n",
    "scaler = StandardScaler()\n",
    "X_train_scaled = scaler.fit_transform(X_train)\n",
    "X_test_scaled = scaler.transform(X_test)\n",
    "\n",
    "# Train the SVM model\n",
    "svm_model = SVC(kernel='rbf', gamma=0.001, C=10)\n",
    "svm_model.fit(X_train_scaled, y_train)\n",
    "\n",
    "# Make predictions\n",
    "y_pred = svm_model.predict(X_test_scaled)\n",
    "\n",
    "# Evaluation\n",
    "print(\"Classification Report:\\n\", classification_report(y_test, y_pred))\n",
    "print(\"Confusion Matrix:\\n\", confusion_matrix(y_test, y_pred))\n",
    "\n",
    "# Display some predicted digits\n",
    "plt.figure(figsize=(10, 4))\n",
    "for index, (image, prediction) in enumerate(zip(X_test[:8], y_pred[:8])):\n",
    "    plt.subplot(2, 4, index + 1)\n",
    "    plt.imshow(image.reshape(8, 8), cmap=plt.cm.gray_r)\n",
    "    plt.title(f\"Pred: {prediction}\")\n",
    "    plt.axis('off')\n",
    "plt.tight_layout()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "770e4d5d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
