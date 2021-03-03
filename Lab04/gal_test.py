{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def __init__(self, gal_file):  \n",
    "    \n",
    "    # get file name\n",
    "    self.gal_file = gal_file   \n",
    "    \n",
    "    # open and read gal file\n",
    "    fp = open(gal_file)        \n",
    "    lines = fp.readlines()\n",
    "    fp.close()\n",
    "    self.lines = lines\n",
    "    \n",
    "    # build the dictionary\n",
    "    line0 = lines[0]            \n",
    "    line0 = line0.strip().split()\n",
    "    self.line0 = line0\n",
    "    self.n_polygons = int(line0[1])\n",
    "    neighbors = {}\n",
    "    lines = lines[1:]\n",
    "    processing = True \n",
    "    i = 0\n",
    "    while i < self.n_polygons * 2:\n",
    "        header = lines[i].strip().split()\n",
    "        i_neighbors = lines[i+1].strip().split()\n",
    "        node_i = header[0]\n",
    "        neighbors[node_i] = i_neighbors\n",
    "        i += 2\n",
    "    self.neighbors = neighbors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
