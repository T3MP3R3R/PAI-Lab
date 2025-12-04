# -----------------------------
# Object-Oriented Programming (OOP)
# -----------------------------
class Player:
    team = "India"  # class variable shared by all

    def __init__(self, name, runs, matches):
        self.name = name        # instance variable
        self.runs = runs
        self.matches = matches

    # Instance method
    def greet(self):
        return f"Hi, I'm {self.name} from {Player.team}"

    # Instance method
    def add_runs(self, r):
        self.runs += r

    # Magic methods
    def __str__(self):
        return f"Player({self.name}, Runs:{self.runs}, Matches:{self.matches})"

    def __eq__(self, other):
        return self.runs == other.runs

    # Class method
    @classmethod
    def change_team(cls, new_team):
        cls.team = new_team

    # Static method
    @staticmethod
    def game_type():
        return "Test, ODI, T20"

# -----------------------------
# Inheritance
# -----------------------------
class Captain(Player):
    def __init__(self, name, runs, matches, leadership_score):
        super().__init__(name, runs, matches)
        self.leadership_score = leadership_score

    # Overriding
    def greet(self):
        return f"I'm Captain {self.name} with leadership {self.leadership_score}"

    # Polymorphism example: method signature same as parent but behavior different
    def add_runs(self, r):
        super().add_runs(r)
        self.leadership_score += r*0.1  # leadership grows with runs

# -----------------------------
# Encapsulation / Private attributes
# -----------------------------
class Stats:
    def __init__(self, runs, wickets):
        self.__runs = runs     # private
        self.__wickets = wickets  # private

    # Getter
    def get_runs(self):
        return self.__runs

    # Setter
    def set_runs(self, val):
        if val >= 0:
            self.__runs = val

stats = Stats(1000, 50)
stats.set_runs(1200)
print(stats.get_runs())

# -----------------------------
# Polymorphism / Duck Typing
# -----------------------------
class Batsman:
    def play(self):
        print("Batsman scores runs")

class Bowler:
    def play(self):
        print("Bowler bowls well")

players = [Batsman(), Bowler()]
for p in players:
    p.play()   # same method name, different behavior (polymorphism)

# -----------------------------
# Multiple Inheritance
# -----------------------------
class Coach:
    def advise(self):
        print("Train harder!")

class PlayerCoach(Player, Coach):
    pass

pc = PlayerCoach("Alex", 500, 20)
pc.greet()
pc.advise()

# -----------------------------
# OOP Examples
# -----------------------------
p1 = Player("Virat", 1000, 50)
p2 = Player("Rohit", 1000, 60)
print(p1 == p2)   # __eq__ magic method
Player.change_team("India A")
print(p1.greet())
print(Player.game_type())

c = Captain("Kohli", 1200, 70, 95)
c.add_runs(50)
print(c.greet(), c.leadership_score)

# -----------------------------
# 2️⃣ APIs (cricketdata.org example)
# -----------------------------
import requests

API_KEY = "YOUR_API_KEY"

# Fetch live matches
matches_url = f"https://cricapi.com/api/matches?apikey={API_KEY}"
matches_response = requests.get(matches_url)
matches_data = matches_response.json()

# Safely get matches
for match in matches_data.get("matches", [])[:5]:
    print(match.get("team-1",""), "vs", match.get("team-2",""), "at", match.get("date","N/A"))

# Fetch player stats
player_pid = 253802
player_url = f"https://cricapi.com/api/playerStats?apikey={API_KEY}&pid={player_pid}"
player_data = requests.get(player_url).json()

print(player_data.get('name','N/A'))
batting_stats = player_data.get('batting', {})
print("Runs:", batting_stats.get('runs','N/A'), "Average:", batting_stats.get('average','N/A'))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# NumPy
# -----------------------------
arr = np.array([1,2,3,4,5])
print("Array:", arr)
print("Mean:", arr.mean(), "Sum:", arr.sum(), "Max:", arr.max(), "Min:", arr.min())

# Reshape
arr2d = arr.reshape(5,1)
print("Reshaped:\n", arr2d)

# Random arrays
rand_arr = np.random.rand(3,3)  # float 0-1
rand_int = np.random.randint(0,10,(3,3))
print(rand_arr, rand_int)

# Element-wise operations
arr_plus_10 = arr + 10
arr_squared = arr ** 2
print(arr_plus_10, arr_squared)

# Indexing & slicing
print(arr[1:4], arr[::2])

# -----------------------------
# Pandas
# -----------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, np.nan, 28, 22],
    "Salary": [50000, 60000, 55000, np.nan, 45000],
    "Dept": ["HR","IT","IT","Finance","HR"]
}

df = pd.DataFrame(data)
print(df.head(), "\n", df.describe())

# Handling missing data
df.fillna(0, inplace=True)   # or df.dropna(inplace=True)

# Column operations
df["NewSalary"] = df["Salary"] * 1.1
df["AgePlusTen"] = df["Age"] + 10
print(df[["Name","NewSalary"]])

# Filtering
high_salary = df[df["Salary"] > 50000]
print(high_salary)

# Grouping / Aggregation
grouped = df.groupby("Dept")["Salary"].mean()
print(grouped)

# -----------------------------
# Matplotlib
# -----------------------------
plt.figure(figsize=(6,4))

# Line plot
plt.plot(df["Age"], df["Salary"], marker='o', label="Age vs Salary")

# Scatter
plt.scatter(df["Age"], df["Salary"], color='red')

# Bar chart
plt.bar(df["Name"], df["Salary"], color='cyan')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Matplotlib Basics")
plt.legend()
plt.show()

# -----------------------------
# Seaborn
# -----------------------------
# Histogram with KDE
sns.histplot(df["Salary"], kde=True)
plt.show()

# Boxplot
sns.boxplot(x="Dept", y="Salary", data=df)
plt.show()

# Heatmap for correlation
df_corr = df[["Age","Salary","NewSalary"]].corr()
sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.show()

# Pairplot
sns.pairplot(df)
plt.show()

# -----------------------------
# Data Preprocessing Tips
# -----------------------------
# Convert categorical to numeric
df["Dept_code"] = df["Dept"].astype('category').cat.codes

# Standardization / Normalization
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[["Age","Salary"]])
print(df_scaled)

minmax = MinMaxScaler()
df_norm = minmax.fit_transform(df[["Age","Salary"]])
print(df_norm)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

# -----------------------------
# Linear Regression (Simple)
# -----------------------------
# Dataset
X = np.array([[1.1],[1.3],[1.5],[2.0],[2.2],[2.9],[3.0],[3.2],[3.2],[3.7]])
y = np.array([39,46,47,52,56,64,65,67,68,70])

lr = LinearRegression()
lr.fit(X, y)
print("Simple LR -> Coef:", lr.coef_[0], "Intercept:", lr.intercept_)

# Predict salary for 4.5 years
pred = lr.predict([[4.5]])
print("Predicted Salary:", pred[0])

# R²
r2 = lr.score(X, y)
print("R²:", r2)

# -----------------------------
# Multiple Regression
# -----------------------------
# Sample dataset
data = {
    "YearsExp":[1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7],
    "Age":[22,23,25,24,26,30,29,31,30,32],
    "Salary":[39,46,47,52,56,64,65,67,68,70]
}
df = pd.DataFrame(data)
X_multi = df[["YearsExp","Age"]]
y_multi = df["Salary"]

lr_multi = LinearRegression()
lr_multi.fit(X_multi, y_multi)
print("Multiple LR -> Coef:", lr_multi.coef_, "Intercept:", lr_multi.intercept_)

# Predict
pred_multi = lr_multi.predict([[4.5,33]])
print("Predicted Salary (Multiple):", pred_multi[0])

# -----------------------------
# Decision Tree Regression
# -----------------------------
X_tree = df[["YearsExp"]]
y_tree = df["Salary"]

tree = DecisionTreeRegressor(random_state=0)
tree.fit(X_tree, y_tree)

pred_tree = tree.predict([[4.5]])
print("Decision Tree Prediction:", pred_tree[0])

# -----------------------------
# 4️⃣ K-Means Clustering
# -----------------------------
X_cluster = df[["YearsExp","Salary"]]
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_cluster)

df["Cluster"] = kmeans.labels_
print(df)

# Predict cluster for new data
new_point = np.array([[4.5, 75]])
cluster_label = kmeans.predict(new_point)
print("Cluster Label for new point:", cluster_label[0])

# -----------------------------
# 5️⃣ ML Tips / Metrics
# -----------------------------
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# ==============================
# 5️⃣ Computer Vision (OpenCV) Cheatsheet
# ==============================

import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # Only for Colab

# -----------------------------
# Load & Display Image
# -----------------------------
img_path = "example.jpg"  # Replace with your image path
img = cv2.imread(img_path)

if img is None:
    print("Image not found")
else:
    cv2_imshow(img)  # Display original image

# -----------------------------
# Grayscale & Resize
# -----------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)

resized = cv2.resize(img, (300, 200))  # width=300, height=200
cv2_imshow(resized)

# -----------------------------
# Crop & Gaussian Blur
# -----------------------------
cropped = img[50:250, 100:400]  # y1:y2, x1:x2
cv2_imshow(cropped)

blurred = cv2.GaussianBlur(img, (5,5), 0)
cv2_imshow(blurred)

# -----------------------------
# Create Blank Image & Draw Shapes
# -----------------------------
blank = np.zeros((300,300,3), dtype=np.uint8)

# Draw rectangle
cv2.rectangle(blank, (50,50), (250,150), (0,255,0), 3) # BGR, thickness=3

# Draw circle
cv2.circle(blank, (150,200), 50, (255,0,0), -1) # filled circle

# Draw line
cv2.line(blank, (0,0), (300,300), (0,0,255), 2)

# Add text
cv2.putText(blank, "Hello OpenCV", (20,280), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
cv2_imshow(blank)

# -----------------------------
# Add Text to Existing Image
# -----------------------------
cv2.putText(img, "Sample Text", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
cv2_imshow(img)

# ==============================
# Analyzing Image Pixel Values with Pandas (RGB)
# ==============================
# Convert RGB image to DataFrame (flatten pixels)
    image_df = pd.DataFrame(image.reshape(-1, 3), columns=['B','G','R'])

    # Display basic statistics
    print("Basic Statistics of Image Pixel Values:")
    print(image_df.describe())

    # Pixel value histogram per channel
    image_df.hist(figsize=(12,4))
    plt.suptitle("Pixel Value Distribution per Channel")
    plt.show()

    # Access/manipulate specific pixels
    row, col = 100, 150
    print(f"Pixel at ({row},{col}):", image[row, col])  # Returns [B,G,R]

    # Example: increase red channel for all pixels
    image_df['R'] = image_df['R'] + 50
    image_df['R'] = image_df['R'].clip(0,255)  # keep values 0-255
    modified_img = image_df.to_numpy().reshape(image.shape).astype(np.uint8)
    cv2_imshow(modified_img)

# -----------------------------
# Binary Thresholding
# -----------------------------
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2_imshow(thresh)

# -----------------------------
# Rotate Image
# -----------------------------
(h, w) = img.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 60, 1.0)  # rotate 60 deg, scale=1
rotated = cv2.warpAffine(img, M, (w,h))
cv2_imshow(rotated)

# -----------------------------
# Image Blending
# -----------------------------
img2 = cv2.imread("example2.jpg")  # Replace with second image
img2 = cv2.resize(img2, (w,h))
blended = cv2.addWeighted(img, 0.7, img2, 0.3, 0)  # alpha, beta, gamma
cv2_imshow(blended)

# -----------------------------
# Histogram Equalization
# -----------------------------
gray_blend = cv2.cvtColor(blended, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray_blend)
cv2_imshow(equalized)

# -----------------------------
# Quick Tips
# -----------------------------
# Save image
cv2.imwrite("output.jpg", equalized)

# Convert color spaces
# cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Access pixel
px = img[100,100]  # BGR value at (100,100)
img[100,100] = [255,255,255]  # change pixel

# Resize maintaining aspect ratio
scale = 0.5
new_dim = (int(w*scale), int(h*scale))
resized_aspect = cv2.resize(img, new_dim)
cv2_imshow(resized_aspect)
