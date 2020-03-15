# RestaurantFeedbackClassification
<h2>Reviewing Restaurant feedbacks and classifying them as good and bad and comparing the results of various classification algorithms for natural language processing.</h2>
<hr>
<h4>Gaussian Naive Bayes Implementation: </h4>
<table>
<tr>
<td><b>Classification Report:</b></td>
<td>precision</td>
<td>recall</td>
<td>f1-score</td>
<td>support</td>
</tr>

<tr>
<td>0</td>
<td>0.81</td>
<td>0.58</td>
<td>0.68</td>
<td>98</td>
</tr>

<tr>
<td>1</td>
<td>0.68</td>
<td>0.87</td>
<td>0.77</td>
<td>102</td>
</tr>

<tr>
<td>accuracy</td>
<td></td>
<td></td>
<td>0.73</td>
<td>200</td>
</tr>


<tr>
<td>macro avg</td>
<td>0.75</td>
<td>0.73</td>
<td>0.72</td>
<td>200</td>
</tr>


<tr>
<td>weighted avg</td>
<td>0.75</td>
<td>0.73</td>
<td>0.72</td>
<td>200</td>
</tr>
</table>

<b>Confusion Matrix: </b><br>
  [[57 41] <br>
 [13 89]]
 
<b>Accuracy Score: </b>
 0.73

<hr>
<h4>Decision Tree Implementation: </h4>

<table>
<tr>
<td><b>Classification Report:</b></td>
<td>precision</td>
<td>recall</td>
<td>f1-score</td>
<td>support</td>
</tr>

<tr>
<td>0</td>
<td>0.71</td>
<td>0.73</td>
<td>0.72</td>
<td>93</td>
</tr>

<tr>
<td>1</td>
<td>0.76</td>
<td>0.74</td>
<td>0.75</td>
<td>107</td>
</tr>

<tr>
<td>accuracy</td>
<td></td>
<td></td>
<td>0.73</td>
<td>200</td>
</tr>

<tr>
<td>macro avg</td>
<td>0.73</td>
<td>0.73</td>
<td>0.73</td>
<td>200</td>
</tr>


<tr>
<td>weighted avg</td>
<td>0.74</td>
<td>0.73</td>
<td>0.74</td>
<td>200</td>
</tr>
</table>

<b>Confusion Matrix: </b><br>
 [[68 25] <br>
 [28 79]]
 
<b>Accuracy Score: </b>
 0.735
 
 <hr>
<h4>Random Forest Implementation: </h4>

<table>
<tr>
<td><b>Classification Report:</b></td>
<td>precision</td>
<td>recall</td>
<td>f1-score</td>
<td>support</td>
</tr>

<tr>
<td>0</td>
<td>0.83</td>
<td>0.83</td>
<td>0.83</td>
<td>108</td>
</tr>

<tr>
<td>1</td>
<td>0.80</td>
<td>0.79</td>
<td>0.80</td>
<td>92</td>
</tr>

<tr>
<td>accuracy</td>
<td></td>
<td></td>
<td>0.81</td>
<td>200</td>
</tr>

<tr>
<td>macro avg</td>
<td>0.81</td>
<td>0.81</td>
<td>0.81</td>
<td>200</td>
</tr>


<tr>
<td>weighted avg</td>
<td>0.81</td>
<td>0.81</td>
<td>0.81</td>
<td>200</td>
</tr>
</table>

<b>Confusion Matrix: </b><br>
 [[90 18] <br>
 [19 73]]
 
<b>Accuracy Score: </b>
 0.815
 
 
