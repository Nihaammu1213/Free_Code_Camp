{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92ebf528",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def calculate(list):\n",
    "    if len(list) != 9:\n",
    "        raise ValueError('List must contain nine numbers.')\n",
    "    else:\n",
    "        matrix = np.array(list).reshape(3, 3)\n",
    "\n",
    "    mean = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()),\n",
    "            (matrix.flatten().mean())]\n",
    "\n",
    "    var = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()),\n",
    "           (matrix.flatten().var())]\n",
    "    std = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()),\n",
    "           (matrix.flatten().std())]\n",
    "\n",
    "    max = [(matrix.max(axis=0).tolist()), (matrix.max(axis=1).tolist()),\n",
    "           (matrix.flatten().max())]\n",
    "\n",
    "    min = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()),\n",
    "           (matrix.flatten().min())]\n",
    "\n",
    "    sum = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()),\n",
    "           (matrix.flatten().sum())]\n",
    "\n",
    "    calculations = {\n",
    "        \"mean\": mean,\n",
    "        \"variance\": var,\n",
    "        \"standard deviation\":std,\n",
    "        \"max\": max,\n",
    "        \"min\": min,\n",
    "        \"sum\": sum,\n",
    "    }\n",
    "    return calculations\n",
    "\n"
   ]
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
