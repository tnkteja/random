

```python
url="https://raw.githubusercontent.com/tnkteja/random/master/dataset_1.csv"
```


```python
import pandas as pd
import numpy as np
```


```python
df=pd.read_csv(url)
```


```python
del df["Id"]
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>RL</td>
      <td>85.0</td>
      <td>14115</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>Shed</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>10084</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>RL</td>
      <td>NaN</td>
      <td>10382</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>RM</td>
      <td>51.0</td>
      <td>6120</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>RL</td>
      <td>50.0</td>
      <td>7420</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>RL</td>
      <td>70.0</td>
      <td>11200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>RL</td>
      <td>85.0</td>
      <td>11924</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>New</td>
      <td>Partial</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>12968</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR2</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>RL</td>
      <td>91.0</td>
      <td>10652</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>New</td>
      <td>Partial</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>10920</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>RM</td>
      <td>51.0</td>
      <td>6120</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>11241</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>RL</td>
      <td>72.0</td>
      <td>10791</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>RL</td>
      <td>66.0</td>
      <td>13695</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>RL</td>
      <td>70.0</td>
      <td>7560</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>COD</td>
      <td>Abnorml</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>RL</td>
      <td>101.0</td>
      <td>14215</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>New</td>
      <td>Partial</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>RM</td>
      <td>57.0</td>
      <td>7449</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9742</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>RM</td>
      <td>44.0</td>
      <td>4224</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>8246</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>RL</td>
      <td>110.0</td>
      <td>14230</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>RL</td>
      <td>60.0</td>
      <td>7200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>RL</td>
      <td>98.0</td>
      <td>11478</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>RL</td>
      <td>47.0</td>
      <td>16321</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>RM</td>
      <td>60.0</td>
      <td>6324</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>RL</td>
      <td>60.0</td>
      <td>21930</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR3</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>RL</td>
      <td>NaN</td>
      <td>4928</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>RL</td>
      <td>60.0</td>
      <td>10800</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>RL</td>
      <td>93.0</td>
      <td>10261</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>17400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>8400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>COD</td>
      <td>Abnorml</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>RL</td>
      <td>96.0</td>
      <td>12444</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>New</td>
      <td>Partial</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>RM</td>
      <td>90.0</td>
      <td>7407</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>11584</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>RL</td>
      <td>79.0</td>
      <td>11526</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>RM</td>
      <td>NaN</td>
      <td>4426</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>FV</td>
      <td>85.0</td>
      <td>11003</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>RL</td>
      <td>NaN</td>
      <td>8854</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>RL</td>
      <td>63.0</td>
      <td>8500</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>RL</td>
      <td>70.0</td>
      <td>8400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>26142</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>10000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>RL</td>
      <td>70.0</td>
      <td>11767</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>RM</td>
      <td>21.0</td>
      <td>1533</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>RL</td>
      <td>78.0</td>
      <td>9262</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>New</td>
      <td>Partial</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>RM</td>
      <td>35.0</td>
      <td>3675</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>RL</td>
      <td>90.0</td>
      <td>17217</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>FV</td>
      <td>62.0</td>
      <td>7500</td>
      <td>Pave</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>RL</td>
      <td>62.0</td>
      <td>7917</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>RL</td>
      <td>85.0</td>
      <td>13175</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>RL</td>
      <td>66.0</td>
      <td>9042</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>Shed</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>RL</td>
      <td>68.0</td>
      <td>9717</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9937</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 80 columns</p>
</div>




```python
dfcv=df.columns.values
dfcvl=list(dfcv)
cDF=pd.DataFrame(df.columns.values)
cDF
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSSubClass</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSZoning</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LotFrontage</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LotArea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Street</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Alley</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LotShape</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LandContour</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Utilities</td>
    </tr>
    <tr>
      <th>9</th>
      <td>LotConfig</td>
    </tr>
    <tr>
      <th>10</th>
      <td>LandSlope</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Neighborhood</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Condition1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Condition2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>BldgType</td>
    </tr>
    <tr>
      <th>15</th>
      <td>HouseStyle</td>
    </tr>
    <tr>
      <th>16</th>
      <td>OverallQual</td>
    </tr>
    <tr>
      <th>17</th>
      <td>OverallCond</td>
    </tr>
    <tr>
      <th>18</th>
      <td>YearBuilt</td>
    </tr>
    <tr>
      <th>19</th>
      <td>YearRemodAdd</td>
    </tr>
    <tr>
      <th>20</th>
      <td>RoofStyle</td>
    </tr>
    <tr>
      <th>21</th>
      <td>RoofMatl</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Exterior1st</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Exterior2nd</td>
    </tr>
    <tr>
      <th>24</th>
      <td>MasVnrType</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MasVnrArea</td>
    </tr>
    <tr>
      <th>26</th>
      <td>ExterQual</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ExterCond</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Foundation</td>
    </tr>
    <tr>
      <th>29</th>
      <td>BsmtQual</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>50</th>
      <td>BedroomAbvGr</td>
    </tr>
    <tr>
      <th>51</th>
      <td>KitchenAbvGr</td>
    </tr>
    <tr>
      <th>52</th>
      <td>KitchenQual</td>
    </tr>
    <tr>
      <th>53</th>
      <td>TotRmsAbvGrd</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Functional</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Fireplaces</td>
    </tr>
    <tr>
      <th>56</th>
      <td>FireplaceQu</td>
    </tr>
    <tr>
      <th>57</th>
      <td>GarageType</td>
    </tr>
    <tr>
      <th>58</th>
      <td>GarageYrBlt</td>
    </tr>
    <tr>
      <th>59</th>
      <td>GarageFinish</td>
    </tr>
    <tr>
      <th>60</th>
      <td>GarageCars</td>
    </tr>
    <tr>
      <th>61</th>
      <td>GarageArea</td>
    </tr>
    <tr>
      <th>62</th>
      <td>GarageQual</td>
    </tr>
    <tr>
      <th>63</th>
      <td>GarageCond</td>
    </tr>
    <tr>
      <th>64</th>
      <td>PavedDrive</td>
    </tr>
    <tr>
      <th>65</th>
      <td>WoodDeckSF</td>
    </tr>
    <tr>
      <th>66</th>
      <td>OpenPorchSF</td>
    </tr>
    <tr>
      <th>67</th>
      <td>EnclosedPorch</td>
    </tr>
    <tr>
      <th>68</th>
      <td>3SsnPorch</td>
    </tr>
    <tr>
      <th>69</th>
      <td>ScreenPorch</td>
    </tr>
    <tr>
      <th>70</th>
      <td>PoolArea</td>
    </tr>
    <tr>
      <th>71</th>
      <td>PoolQC</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Fence</td>
    </tr>
    <tr>
      <th>73</th>
      <td>MiscFeature</td>
    </tr>
    <tr>
      <th>74</th>
      <td>MiscVal</td>
    </tr>
    <tr>
      <th>75</th>
      <td>MoSold</td>
    </tr>
    <tr>
      <th>76</th>
      <td>YrSold</td>
    </tr>
    <tr>
      <th>77</th>
      <td>SaleType</td>
    </tr>
    <tr>
      <th>78</th>
      <td>SaleCondition</td>
    </tr>
    <tr>
      <th>79</th>
      <td>SalePrice</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 1 columns</p>
</div>




```python
df.dtypes
```




    MSSubClass         int64
    MSZoning          object
    LotFrontage      float64
    LotArea            int64
    Street            object
    Alley             object
    LotShape          object
    LandContour       object
    Utilities         object
    LotConfig         object
    LandSlope         object
    Neighborhood      object
    Condition1        object
    Condition2        object
    BldgType          object
    HouseStyle        object
    OverallQual        int64
    OverallCond        int64
    YearBuilt          int64
    YearRemodAdd       int64
    RoofStyle         object
    RoofMatl          object
    Exterior1st       object
    Exterior2nd       object
    MasVnrType        object
    MasVnrArea       float64
    ExterQual         object
    ExterCond         object
    Foundation        object
    BsmtQual          object
                      ...   
    BedroomAbvGr       int64
    KitchenAbvGr       int64
    KitchenQual       object
    TotRmsAbvGrd       int64
    Functional        object
    Fireplaces         int64
    FireplaceQu       object
    GarageType        object
    GarageYrBlt      float64
    GarageFinish      object
    GarageCars         int64
    GarageArea         int64
    GarageQual        object
    GarageCond        object
    PavedDrive        object
    WoodDeckSF         int64
    OpenPorchSF        int64
    EnclosedPorch      int64
    3SsnPorch          int64
    ScreenPorch        int64
    PoolArea           int64
    PoolQC            object
    Fence             object
    MiscFeature       object
    MiscVal            int64
    MoSold             int64
    YrSold             int64
    SaleType          object
    SaleCondition     object
    SalePrice          int64
    dtype: object




```python
df.select_dtypes(include=[np.number])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>OverallQual</th>
      <th>OverallCond</th>
      <th>YearBuilt</th>
      <th>YearRemodAdd</th>
      <th>MasVnrArea</th>
      <th>BsmtFinSF1</th>
      <th>BsmtFinSF2</th>
      <th>...</th>
      <th>WoodDeckSF</th>
      <th>OpenPorchSF</th>
      <th>EnclosedPorch</th>
      <th>3SsnPorch</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>65.0</td>
      <td>8450</td>
      <td>7</td>
      <td>5</td>
      <td>2003</td>
      <td>2003</td>
      <td>196.0</td>
      <td>706</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>61</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>80.0</td>
      <td>9600</td>
      <td>6</td>
      <td>8</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>978</td>
      <td>0</td>
      <td>...</td>
      <td>298</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>68.0</td>
      <td>11250</td>
      <td>7</td>
      <td>5</td>
      <td>2001</td>
      <td>2002</td>
      <td>162.0</td>
      <td>486</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>60.0</td>
      <td>9550</td>
      <td>7</td>
      <td>5</td>
      <td>1915</td>
      <td>1970</td>
      <td>0.0</td>
      <td>216</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>35</td>
      <td>272</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>84.0</td>
      <td>14260</td>
      <td>8</td>
      <td>5</td>
      <td>2000</td>
      <td>2000</td>
      <td>350.0</td>
      <td>655</td>
      <td>0</td>
      <td>...</td>
      <td>192</td>
      <td>84</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>85.0</td>
      <td>14115</td>
      <td>5</td>
      <td>5</td>
      <td>1993</td>
      <td>1995</td>
      <td>0.0</td>
      <td>732</td>
      <td>0</td>
      <td>...</td>
      <td>40</td>
      <td>30</td>
      <td>0</td>
      <td>320</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>75.0</td>
      <td>10084</td>
      <td>8</td>
      <td>5</td>
      <td>2004</td>
      <td>2005</td>
      <td>186.0</td>
      <td>1369</td>
      <td>0</td>
      <td>...</td>
      <td>255</td>
      <td>57</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>0.0</td>
      <td>10382</td>
      <td>7</td>
      <td>6</td>
      <td>1973</td>
      <td>1973</td>
      <td>240.0</td>
      <td>859</td>
      <td>32</td>
      <td>...</td>
      <td>235</td>
      <td>204</td>
      <td>228</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>51.0</td>
      <td>6120</td>
      <td>7</td>
      <td>5</td>
      <td>1931</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>90</td>
      <td>0</td>
      <td>205</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>50.0</td>
      <td>7420</td>
      <td>5</td>
      <td>6</td>
      <td>1939</td>
      <td>1950</td>
      <td>0.0</td>
      <td>851</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>70.0</td>
      <td>11200</td>
      <td>5</td>
      <td>5</td>
      <td>1965</td>
      <td>1965</td>
      <td>0.0</td>
      <td>906</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>85.0</td>
      <td>11924</td>
      <td>9</td>
      <td>5</td>
      <td>2005</td>
      <td>2006</td>
      <td>286.0</td>
      <td>998</td>
      <td>0</td>
      <td>...</td>
      <td>147</td>
      <td>21</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>0.0</td>
      <td>12968</td>
      <td>5</td>
      <td>6</td>
      <td>1962</td>
      <td>1962</td>
      <td>0.0</td>
      <td>737</td>
      <td>0</td>
      <td>...</td>
      <td>140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>176</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>91.0</td>
      <td>10652</td>
      <td>7</td>
      <td>5</td>
      <td>2006</td>
      <td>2007</td>
      <td>306.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>160</td>
      <td>33</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>0.0</td>
      <td>10920</td>
      <td>6</td>
      <td>5</td>
      <td>1960</td>
      <td>1960</td>
      <td>212.0</td>
      <td>733</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>213</td>
      <td>176</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>51.0</td>
      <td>6120</td>
      <td>7</td>
      <td>8</td>
      <td>1929</td>
      <td>2001</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>48</td>
      <td>112</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>0.0</td>
      <td>11241</td>
      <td>6</td>
      <td>7</td>
      <td>1970</td>
      <td>1970</td>
      <td>180.0</td>
      <td>578</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>72.0</td>
      <td>10791</td>
      <td>4</td>
      <td>5</td>
      <td>1967</td>
      <td>1967</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>66.0</td>
      <td>13695</td>
      <td>5</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>0.0</td>
      <td>646</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>102</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>70.0</td>
      <td>7560</td>
      <td>5</td>
      <td>6</td>
      <td>1958</td>
      <td>1965</td>
      <td>0.0</td>
      <td>504</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>101.0</td>
      <td>14215</td>
      <td>8</td>
      <td>5</td>
      <td>2005</td>
      <td>2006</td>
      <td>380.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>240</td>
      <td>154</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>57.0</td>
      <td>7449</td>
      <td>7</td>
      <td>7</td>
      <td>1930</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>205</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>75.0</td>
      <td>9742</td>
      <td>8</td>
      <td>5</td>
      <td>2002</td>
      <td>2002</td>
      <td>281.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>171</td>
      <td>159</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>44.0</td>
      <td>4224</td>
      <td>5</td>
      <td>7</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>840</td>
      <td>0</td>
      <td>...</td>
      <td>100</td>
      <td>110</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>0.0</td>
      <td>8246</td>
      <td>5</td>
      <td>8</td>
      <td>1968</td>
      <td>2001</td>
      <td>0.0</td>
      <td>188</td>
      <td>668</td>
      <td>...</td>
      <td>406</td>
      <td>90</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>110.0</td>
      <td>14230</td>
      <td>8</td>
      <td>5</td>
      <td>2007</td>
      <td>2007</td>
      <td>640.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>56</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>60.0</td>
      <td>7200</td>
      <td>5</td>
      <td>7</td>
      <td>1951</td>
      <td>2000</td>
      <td>0.0</td>
      <td>234</td>
      <td>486</td>
      <td>...</td>
      <td>222</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>98.0</td>
      <td>11478</td>
      <td>8</td>
      <td>5</td>
      <td>2007</td>
      <td>2008</td>
      <td>200.0</td>
      <td>1218</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>47.0</td>
      <td>16321</td>
      <td>5</td>
      <td>6</td>
      <td>1957</td>
      <td>1997</td>
      <td>0.0</td>
      <td>1277</td>
      <td>0</td>
      <td>...</td>
      <td>288</td>
      <td>258</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>60.0</td>
      <td>6324</td>
      <td>4</td>
      <td>6</td>
      <td>1927</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>49</td>
      <td>0</td>
      <td>87</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>60.0</td>
      <td>21930</td>
      <td>5</td>
      <td>5</td>
      <td>2005</td>
      <td>2005</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>100</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>0.0</td>
      <td>4928</td>
      <td>6</td>
      <td>6</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>958</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>60.0</td>
      <td>10800</td>
      <td>4</td>
      <td>6</td>
      <td>1927</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>93.0</td>
      <td>10261</td>
      <td>6</td>
      <td>5</td>
      <td>2000</td>
      <td>2000</td>
      <td>318.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>80.0</td>
      <td>17400</td>
      <td>5</td>
      <td>5</td>
      <td>1977</td>
      <td>1977</td>
      <td>0.0</td>
      <td>936</td>
      <td>0</td>
      <td>...</td>
      <td>295</td>
      <td>41</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>80.0</td>
      <td>8400</td>
      <td>6</td>
      <td>9</td>
      <td>1962</td>
      <td>2005</td>
      <td>237.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>60.0</td>
      <td>9000</td>
      <td>4</td>
      <td>6</td>
      <td>1971</td>
      <td>1971</td>
      <td>0.0</td>
      <td>616</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>96.0</td>
      <td>12444</td>
      <td>8</td>
      <td>5</td>
      <td>2008</td>
      <td>2008</td>
      <td>426.0</td>
      <td>1336</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>66</td>
      <td>0</td>
      <td>304</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>90.0</td>
      <td>7407</td>
      <td>6</td>
      <td>7</td>
      <td>1957</td>
      <td>1996</td>
      <td>0.0</td>
      <td>600</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>158</td>
      <td>158</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>80.0</td>
      <td>11584</td>
      <td>7</td>
      <td>6</td>
      <td>1979</td>
      <td>1979</td>
      <td>96.0</td>
      <td>315</td>
      <td>110</td>
      <td>...</td>
      <td>0</td>
      <td>88</td>
      <td>216</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>79.0</td>
      <td>11526</td>
      <td>6</td>
      <td>7</td>
      <td>1922</td>
      <td>1994</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>431</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>0.0</td>
      <td>4426</td>
      <td>6</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>147.0</td>
      <td>697</td>
      <td>0</td>
      <td>...</td>
      <td>149</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>85.0</td>
      <td>11003</td>
      <td>10</td>
      <td>5</td>
      <td>2008</td>
      <td>2008</td>
      <td>160.0</td>
      <td>765</td>
      <td>0</td>
      <td>...</td>
      <td>168</td>
      <td>52</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>0.0</td>
      <td>8854</td>
      <td>6</td>
      <td>6</td>
      <td>1916</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>98</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>63.0</td>
      <td>8500</td>
      <td>7</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>106.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>192</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>70.0</td>
      <td>8400</td>
      <td>6</td>
      <td>5</td>
      <td>1966</td>
      <td>1966</td>
      <td>0.0</td>
      <td>187</td>
      <td>627</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>252</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>0.0</td>
      <td>26142</td>
      <td>5</td>
      <td>7</td>
      <td>1962</td>
      <td>1962</td>
      <td>189.0</td>
      <td>593</td>
      <td>0</td>
      <td>...</td>
      <td>261</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>80.0</td>
      <td>10000</td>
      <td>8</td>
      <td>5</td>
      <td>1995</td>
      <td>1996</td>
      <td>438.0</td>
      <td>1079</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>65</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>70.0</td>
      <td>11767</td>
      <td>4</td>
      <td>7</td>
      <td>1910</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>168</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>21.0</td>
      <td>1533</td>
      <td>5</td>
      <td>7</td>
      <td>1970</td>
      <td>1970</td>
      <td>0.0</td>
      <td>553</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>60.0</td>
      <td>9000</td>
      <td>5</td>
      <td>5</td>
      <td>1974</td>
      <td>1974</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>32</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>78.0</td>
      <td>9262</td>
      <td>8</td>
      <td>5</td>
      <td>2008</td>
      <td>2009</td>
      <td>194.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>35.0</td>
      <td>3675</td>
      <td>5</td>
      <td>5</td>
      <td>2005</td>
      <td>2005</td>
      <td>80.0</td>
      <td>547</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>90.0</td>
      <td>17217</td>
      <td>5</td>
      <td>5</td>
      <td>2006</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>36</td>
      <td>56</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>62.0</td>
      <td>7500</td>
      <td>7</td>
      <td>5</td>
      <td>2004</td>
      <td>2005</td>
      <td>0.0</td>
      <td>410</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>113</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>62.0</td>
      <td>7917</td>
      <td>6</td>
      <td>5</td>
      <td>1999</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>85.0</td>
      <td>13175</td>
      <td>6</td>
      <td>6</td>
      <td>1978</td>
      <td>1988</td>
      <td>119.0</td>
      <td>790</td>
      <td>163</td>
      <td>...</td>
      <td>349</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>66.0</td>
      <td>9042</td>
      <td>7</td>
      <td>9</td>
      <td>1941</td>
      <td>2006</td>
      <td>0.0</td>
      <td>275</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>68.0</td>
      <td>9717</td>
      <td>5</td>
      <td>6</td>
      <td>1950</td>
      <td>1996</td>
      <td>0.0</td>
      <td>49</td>
      <td>1029</td>
      <td>...</td>
      <td>366</td>
      <td>0</td>
      <td>112</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>75.0</td>
      <td>9937</td>
      <td>5</td>
      <td>6</td>
      <td>1965</td>
      <td>1965</td>
      <td>0.0</td>
      <td>830</td>
      <td>290</td>
      <td>...</td>
      <td>736</td>
      <td>68</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 37 columns</p>
</div>




```python
dtdf = pd.DataFrame(df.dtypes, columns=['Data Type'])
dtdf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Data Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>object</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>float64</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>object</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>object</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>object</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>object</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>object</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>object</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>object</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>object</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>object</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>object</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>float64</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>object</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>object</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>object</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>object</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>object</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>object</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>float64</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>object</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>object</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>object</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>object</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>object</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>object</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>object</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>int64</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>object</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>object</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>int64</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 1 columns</p>
</div>




```python
df.isnull()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>13</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>15</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>16</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>17</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>18</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>19</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>20</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>21</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>22</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>23</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>24</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>25</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>26</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>27</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>28</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>29</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>...</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 80 columns</p>
</div>




```python
mdcdf=pd.DataFrame(df.isnull().sum(), columns=['Missing values'])
mdcdf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Missing values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>259</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>1369</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>0</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>0</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>8</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>8</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>0</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>37</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>0</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>0</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>0</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>0</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>690</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>0</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>81</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>0</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>1453</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>1179</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>1406</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 1 columns</p>
</div>




```python
mdcdf[mdcdf["Missing values"] >0].plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5c87e6390>




![png](output_10_1.png)


*Reason* :

*Missing Hypothesis*:


```python
pdcdf = pd.DataFrame(df.count(), columns=['Present Values'])

```


```python
minmaxvsdf=df.describe().loc[["min","max"]].transpose()
```

    /usr/local/lib/python3.5/dist-packages/numpy/lib/function_base.py:3834: RuntimeWarning: Invalid value encountered in percentile
      RuntimeWarning)



```python
uvcdf = pd.DataFrame(columns=['Unique Values'])
for v in dfcvl:
    uvcdf.loc[v] = [df[v].nunique()]
uvcdf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>15.0</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>110.0</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>1073.0</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>25.0</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>9.0</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>8.0</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>8.0</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>10.0</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>9.0</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>112.0</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>61.0</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>8.0</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>15.0</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>16.0</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>327.0</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>8.0</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>12.0</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>7.0</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>97.0</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>441.0</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>274.0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>202.0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>120.0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>20.0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>8.0</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>21.0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>12.0</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>9.0</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>6.0</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>663.0</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 1 columns</p>
</div>




```python
dqdf=dtdf.join(pdcdf).join(mdcdf).join(uvcdf).join(minmaxvsdf)
dqdf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Data Type</th>
      <th>Present Values</th>
      <th>Missing values</th>
      <th>Unique Values</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>float64</td>
      <td>1201</td>
      <td>259</td>
      <td>110.0</td>
      <td>21.0</td>
      <td>313.0</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>1073.0</td>
      <td>1300.0</td>
      <td>215245.0</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>object</td>
      <td>91</td>
      <td>1369</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>25.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>8.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>8.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>112.0</td>
      <td>1872.0</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>61.0</td>
      <td>1950.0</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>8.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>16.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>object</td>
      <td>1452</td>
      <td>8</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>float64</td>
      <td>1452</td>
      <td>8</td>
      <td>327.0</td>
      <td>0.0</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>object</td>
      <td>1423</td>
      <td>37</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>12.0</td>
      <td>2.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>7.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>object</td>
      <td>770</td>
      <td>690</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>object</td>
      <td>1379</td>
      <td>81</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>float64</td>
      <td>1379</td>
      <td>81</td>
      <td>97.0</td>
      <td>1900.0</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>object</td>
      <td>1379</td>
      <td>81</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>441.0</td>
      <td>0.0</td>
      <td>1418.0</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>object</td>
      <td>1379</td>
      <td>81</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>object</td>
      <td>1379</td>
      <td>81</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>274.0</td>
      <td>0.0</td>
      <td>857.0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>202.0</td>
      <td>0.0</td>
      <td>547.0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>120.0</td>
      <td>0.0</td>
      <td>552.0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>20.0</td>
      <td>0.0</td>
      <td>508.0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>76.0</td>
      <td>0.0</td>
      <td>480.0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>738.0</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>object</td>
      <td>7</td>
      <td>1453</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>object</td>
      <td>281</td>
      <td>1179</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>object</td>
      <td>54</td>
      <td>1406</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>21.0</td>
      <td>0.0</td>
      <td>15500.0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>12.0</td>
      <td>1.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>5.0</td>
      <td>2006.0</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>object</td>
      <td>1460</td>
      <td>0</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>int64</td>
      <td>1460</td>
      <td>0</td>
      <td>663.0</td>
      <td>34900.0</td>
      <td>755000.0</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 6 columns</p>
</div>




```python
df.describe().transpose()
```

    /usr/local/lib/python3.5/dist-packages/numpy/lib/function_base.py:3834: RuntimeWarning: Invalid value encountered in percentile
      RuntimeWarning)





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>1460.0</td>
      <td>56.897260</td>
      <td>42.300571</td>
      <td>20.0</td>
      <td>20.00</td>
      <td>50.0</td>
      <td>70.00</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>1201.0</td>
      <td>70.049958</td>
      <td>24.284752</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>313.0</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>1460.0</td>
      <td>10516.828082</td>
      <td>9981.264932</td>
      <td>1300.0</td>
      <td>7553.50</td>
      <td>9478.5</td>
      <td>11601.50</td>
      <td>215245.0</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>1460.0</td>
      <td>6.099315</td>
      <td>1.382997</td>
      <td>1.0</td>
      <td>5.00</td>
      <td>6.0</td>
      <td>7.00</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>1460.0</td>
      <td>5.575342</td>
      <td>1.112799</td>
      <td>1.0</td>
      <td>5.00</td>
      <td>5.0</td>
      <td>6.00</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>1460.0</td>
      <td>1971.267808</td>
      <td>30.202904</td>
      <td>1872.0</td>
      <td>1954.00</td>
      <td>1973.0</td>
      <td>2000.00</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>1460.0</td>
      <td>1984.865753</td>
      <td>20.645407</td>
      <td>1950.0</td>
      <td>1967.00</td>
      <td>1994.0</td>
      <td>2004.00</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>1452.0</td>
      <td>103.685262</td>
      <td>181.066207</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>BsmtFinSF1</th>
      <td>1460.0</td>
      <td>443.639726</td>
      <td>456.098091</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>383.5</td>
      <td>712.25</td>
      <td>5644.0</td>
    </tr>
    <tr>
      <th>BsmtFinSF2</th>
      <td>1460.0</td>
      <td>46.549315</td>
      <td>161.319273</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1474.0</td>
    </tr>
    <tr>
      <th>BsmtUnfSF</th>
      <td>1460.0</td>
      <td>567.240411</td>
      <td>441.866955</td>
      <td>0.0</td>
      <td>223.00</td>
      <td>477.5</td>
      <td>808.00</td>
      <td>2336.0</td>
    </tr>
    <tr>
      <th>TotalBsmtSF</th>
      <td>1460.0</td>
      <td>1057.429452</td>
      <td>438.705324</td>
      <td>0.0</td>
      <td>795.75</td>
      <td>991.5</td>
      <td>1298.25</td>
      <td>6110.0</td>
    </tr>
    <tr>
      <th>1stFlrSF</th>
      <td>1460.0</td>
      <td>1162.626712</td>
      <td>386.587738</td>
      <td>334.0</td>
      <td>882.00</td>
      <td>1087.0</td>
      <td>1391.25</td>
      <td>4692.0</td>
    </tr>
    <tr>
      <th>2ndFlrSF</th>
      <td>1460.0</td>
      <td>346.992466</td>
      <td>436.528436</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>728.00</td>
      <td>2065.0</td>
    </tr>
    <tr>
      <th>LowQualFinSF</th>
      <td>1460.0</td>
      <td>5.844521</td>
      <td>48.623081</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>572.0</td>
    </tr>
    <tr>
      <th>GrLivArea</th>
      <td>1460.0</td>
      <td>1515.463699</td>
      <td>525.480383</td>
      <td>334.0</td>
      <td>1129.50</td>
      <td>1464.0</td>
      <td>1776.75</td>
      <td>5642.0</td>
    </tr>
    <tr>
      <th>BsmtFullBath</th>
      <td>1460.0</td>
      <td>0.425342</td>
      <td>0.518911</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>BsmtHalfBath</th>
      <td>1460.0</td>
      <td>0.057534</td>
      <td>0.238753</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>FullBath</th>
      <td>1460.0</td>
      <td>1.565068</td>
      <td>0.550916</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>HalfBath</th>
      <td>1460.0</td>
      <td>0.382877</td>
      <td>0.502885</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>1460.0</td>
      <td>2.866438</td>
      <td>0.815778</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>3.0</td>
      <td>3.00</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>1460.0</td>
      <td>1.046575</td>
      <td>0.220338</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>1460.0</td>
      <td>6.517808</td>
      <td>1.625393</td>
      <td>2.0</td>
      <td>5.00</td>
      <td>6.0</td>
      <td>7.00</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>1460.0</td>
      <td>0.613014</td>
      <td>0.644666</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>1379.0</td>
      <td>1978.506164</td>
      <td>24.689725</td>
      <td>1900.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>1460.0</td>
      <td>1.767123</td>
      <td>0.747315</td>
      <td>0.0</td>
      <td>1.00</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>1460.0</td>
      <td>472.980137</td>
      <td>213.804841</td>
      <td>0.0</td>
      <td>334.50</td>
      <td>480.0</td>
      <td>576.00</td>
      <td>1418.0</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>1460.0</td>
      <td>94.244521</td>
      <td>125.338794</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>168.00</td>
      <td>857.0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>1460.0</td>
      <td>46.660274</td>
      <td>66.256028</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>25.0</td>
      <td>68.00</td>
      <td>547.0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>1460.0</td>
      <td>21.954110</td>
      <td>61.119149</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>552.0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>1460.0</td>
      <td>3.409589</td>
      <td>29.317331</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>508.0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>1460.0</td>
      <td>15.060959</td>
      <td>55.757415</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>480.0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>1460.0</td>
      <td>2.758904</td>
      <td>40.177307</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>738.0</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>1460.0</td>
      <td>43.489041</td>
      <td>496.123024</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>15500.0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>1460.0</td>
      <td>6.321918</td>
      <td>2.703626</td>
      <td>1.0</td>
      <td>5.00</td>
      <td>6.0</td>
      <td>8.00</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>1460.0</td>
      <td>2007.815753</td>
      <td>1.328095</td>
      <td>2006.0</td>
      <td>2007.00</td>
      <td>2008.0</td>
      <td>2009.00</td>
      <td>2010.0</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>1460.0</td>
      <td>180921.195890</td>
      <td>79442.502883</td>
      <td>34900.0</td>
      <td>129975.00</td>
      <td>163000.0</td>
      <td>214000.00</td>
      <td>755000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe(include=['object']).transpose()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSZoning</th>
      <td>1460</td>
      <td>5</td>
      <td>RL</td>
      <td>1151</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>1460</td>
      <td>2</td>
      <td>Pave</td>
      <td>1454</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>91</td>
      <td>2</td>
      <td>Grvl</td>
      <td>50</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>1460</td>
      <td>4</td>
      <td>Reg</td>
      <td>925</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>1460</td>
      <td>4</td>
      <td>Lvl</td>
      <td>1311</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>1460</td>
      <td>2</td>
      <td>AllPub</td>
      <td>1459</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>1460</td>
      <td>5</td>
      <td>Inside</td>
      <td>1052</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>1460</td>
      <td>3</td>
      <td>Gtl</td>
      <td>1382</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>1460</td>
      <td>25</td>
      <td>NAmes</td>
      <td>225</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>1460</td>
      <td>9</td>
      <td>Norm</td>
      <td>1260</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>1460</td>
      <td>8</td>
      <td>Norm</td>
      <td>1445</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>1460</td>
      <td>5</td>
      <td>1Fam</td>
      <td>1220</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>1460</td>
      <td>8</td>
      <td>1Story</td>
      <td>726</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>1460</td>
      <td>6</td>
      <td>Gable</td>
      <td>1141</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>1460</td>
      <td>8</td>
      <td>CompShg</td>
      <td>1434</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>1460</td>
      <td>15</td>
      <td>VinylSd</td>
      <td>515</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>1460</td>
      <td>16</td>
      <td>VinylSd</td>
      <td>504</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>1452</td>
      <td>4</td>
      <td>None</td>
      <td>864</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>1460</td>
      <td>4</td>
      <td>TA</td>
      <td>906</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>1460</td>
      <td>5</td>
      <td>TA</td>
      <td>1282</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>1460</td>
      <td>6</td>
      <td>PConc</td>
      <td>647</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>1423</td>
      <td>4</td>
      <td>TA</td>
      <td>649</td>
    </tr>
    <tr>
      <th>BsmtCond</th>
      <td>1423</td>
      <td>4</td>
      <td>TA</td>
      <td>1311</td>
    </tr>
    <tr>
      <th>BsmtExposure</th>
      <td>1422</td>
      <td>4</td>
      <td>No</td>
      <td>953</td>
    </tr>
    <tr>
      <th>BsmtFinType1</th>
      <td>1423</td>
      <td>6</td>
      <td>Unf</td>
      <td>430</td>
    </tr>
    <tr>
      <th>BsmtFinType2</th>
      <td>1422</td>
      <td>6</td>
      <td>Unf</td>
      <td>1256</td>
    </tr>
    <tr>
      <th>Heating</th>
      <td>1460</td>
      <td>6</td>
      <td>GasA</td>
      <td>1428</td>
    </tr>
    <tr>
      <th>HeatingQC</th>
      <td>1460</td>
      <td>5</td>
      <td>Ex</td>
      <td>741</td>
    </tr>
    <tr>
      <th>CentralAir</th>
      <td>1460</td>
      <td>2</td>
      <td>Y</td>
      <td>1365</td>
    </tr>
    <tr>
      <th>Electrical</th>
      <td>1459</td>
      <td>5</td>
      <td>SBrkr</td>
      <td>1334</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>1460</td>
      <td>4</td>
      <td>TA</td>
      <td>735</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>1460</td>
      <td>7</td>
      <td>Typ</td>
      <td>1360</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>770</td>
      <td>5</td>
      <td>Gd</td>
      <td>380</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>1379</td>
      <td>6</td>
      <td>Attchd</td>
      <td>870</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>1379</td>
      <td>3</td>
      <td>Unf</td>
      <td>605</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>1379</td>
      <td>5</td>
      <td>TA</td>
      <td>1311</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>1379</td>
      <td>5</td>
      <td>TA</td>
      <td>1326</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>1460</td>
      <td>3</td>
      <td>Y</td>
      <td>1340</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>7</td>
      <td>3</td>
      <td>Gd</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>281</td>
      <td>4</td>
      <td>MnPrv</td>
      <td>157</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>54</td>
      <td>4</td>
      <td>Shed</td>
      <td>49</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>1460</td>
      <td>9</td>
      <td>WD</td>
      <td>1267</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>1460</td>
      <td>6</td>
      <td>Normal</td>
      <td>1198</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.mode().transpose()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>20</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>RL</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>60</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>7200</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>Pave</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>Grvl</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>Reg</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>Lvl</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>AllPub</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>Inside</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>Gtl</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>NAmes</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>Norm</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>Norm</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>1Fam</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>1Story</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>5</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>5</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>2006</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>1950</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>Gable</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>CompShg</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>VinylSd</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>VinylSd</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>None</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>TA</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>TA</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>PConc</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>TA</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>3</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>1</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>TA</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>6</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>Typ</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>0</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>Gd</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>Attchd</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>2005</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>Unf</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>2</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>TA</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>TA</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>Y</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>Gd</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>MnPrv</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>Shed</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>6</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>2009</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>WD</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>Normal</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>140000</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 1 columns</p>
</div>



* Deleting columns with too many nulls


```python
mdcdf
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Missing values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MSZoning</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>259</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Street</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>1369</td>
    </tr>
    <tr>
      <th>LotShape</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LandContour</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Utilities</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LotConfig</th>
      <td>0</td>
    </tr>
    <tr>
      <th>LandSlope</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Neighborhood</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Condition1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Condition2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>BldgType</th>
      <td>0</td>
    </tr>
    <tr>
      <th>HouseStyle</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>RoofStyle</th>
      <td>0</td>
    </tr>
    <tr>
      <th>RoofMatl</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Exterior1st</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Exterior2nd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>8</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>8</td>
    </tr>
    <tr>
      <th>ExterQual</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ExterCond</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Foundation</th>
      <td>0</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>37</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>0</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>0</td>
    </tr>
    <tr>
      <th>KitchenQual</th>
      <td>0</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Functional</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>0</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>690</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>0</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>81</td>
    </tr>
    <tr>
      <th>PavedDrive</th>
      <td>0</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>0</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>1453</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>1179</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>1406</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SaleType</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SaleCondition</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>80 rows × 1 columns</p>
</div>




```python
mdcols=mdcdf[mdcdf["Missing values"] > 0]
mdcols
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Missing values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>LotFrontage</th>
      <td>259</td>
    </tr>
    <tr>
      <th>Alley</th>
      <td>1369</td>
    </tr>
    <tr>
      <th>MasVnrType</th>
      <td>8</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>8</td>
    </tr>
    <tr>
      <th>BsmtQual</th>
      <td>37</td>
    </tr>
    <tr>
      <th>BsmtCond</th>
      <td>37</td>
    </tr>
    <tr>
      <th>BsmtExposure</th>
      <td>38</td>
    </tr>
    <tr>
      <th>BsmtFinType1</th>
      <td>37</td>
    </tr>
    <tr>
      <th>BsmtFinType2</th>
      <td>38</td>
    </tr>
    <tr>
      <th>Electrical</th>
      <td>1</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>690</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>81</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>81</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>1453</td>
    </tr>
    <tr>
      <th>Fence</th>
      <td>1179</td>
    </tr>
    <tr>
      <th>MiscFeature</th>
      <td>1406</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
md=pd.DataFrame(index=mdcols.index, columns=["type","fixup_methodss"])
for col in mdcols.index:
    print(col)
```

    LotFrontage
    Alley
    MasVnrType
    MasVnrArea
    BsmtQual
    BsmtCond
    BsmtExposure
    BsmtFinType1
    BsmtFinType2
    Electrical
    FireplaceQu
    GarageType
    GarageYrBlt
    GarageFinish
    GarageQual
    GarageCond
    PoolQC
    Fence
    MiscFeature


LotFrontage  
types
* missing  not at random

Alley
types
* MNAR

MasVnrType


```python
mdcolsl=list(mdcols.index)
mdcolsl
```




    ['LotFrontage',
     'Alley',
     'MasVnrType',
     'MasVnrArea',
     'BsmtQual',
     'BsmtCond',
     'BsmtExposure',
     'BsmtFinType1',
     'BsmtFinType2',
     'Electrical',
     'FireplaceQu',
     'GarageType',
     'GarageYrBlt',
     'GarageFinish',
     'GarageQual',
     'GarageCond',
     'PoolQC',
     'Fence',
     'MiscFeature']



** Eliminate PoolQc column **


```python
#for col in mdcolsl:
#    del df[col]
```


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>RL</td>
      <td>85.0</td>
      <td>14115</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>Shed</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>10084</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>RL</td>
      <td>NaN</td>
      <td>10382</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>RM</td>
      <td>51.0</td>
      <td>6120</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>RL</td>
      <td>50.0</td>
      <td>7420</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>RL</td>
      <td>70.0</td>
      <td>11200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>RL</td>
      <td>85.0</td>
      <td>11924</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>New</td>
      <td>Partial</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>12968</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR2</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>RL</td>
      <td>91.0</td>
      <td>10652</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>New</td>
      <td>Partial</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>10920</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>RM</td>
      <td>51.0</td>
      <td>6120</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>11241</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>RL</td>
      <td>72.0</td>
      <td>10791</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>RL</td>
      <td>66.0</td>
      <td>13695</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>RL</td>
      <td>70.0</td>
      <td>7560</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>COD</td>
      <td>Abnorml</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>RL</td>
      <td>101.0</td>
      <td>14215</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>New</td>
      <td>Partial</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>RM</td>
      <td>57.0</td>
      <td>7449</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9742</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>RM</td>
      <td>44.0</td>
      <td>4224</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>8246</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>RL</td>
      <td>110.0</td>
      <td>14230</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>RL</td>
      <td>60.0</td>
      <td>7200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>RL</td>
      <td>98.0</td>
      <td>11478</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>RL</td>
      <td>47.0</td>
      <td>16321</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>RM</td>
      <td>60.0</td>
      <td>6324</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>RL</td>
      <td>60.0</td>
      <td>21930</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR3</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>RL</td>
      <td>NaN</td>
      <td>4928</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>RL</td>
      <td>60.0</td>
      <td>10800</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>RL</td>
      <td>93.0</td>
      <td>10261</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>17400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>8400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>COD</td>
      <td>Abnorml</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>RL</td>
      <td>96.0</td>
      <td>12444</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>New</td>
      <td>Partial</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>RM</td>
      <td>90.0</td>
      <td>7407</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>11584</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>RL</td>
      <td>79.0</td>
      <td>11526</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>RM</td>
      <td>NaN</td>
      <td>4426</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>FV</td>
      <td>85.0</td>
      <td>11003</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>RL</td>
      <td>NaN</td>
      <td>8854</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>RL</td>
      <td>63.0</td>
      <td>8500</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>RL</td>
      <td>70.0</td>
      <td>8400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>26142</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>10000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>RL</td>
      <td>70.0</td>
      <td>11767</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>RM</td>
      <td>21.0</td>
      <td>1533</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>RL</td>
      <td>78.0</td>
      <td>9262</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>New</td>
      <td>Partial</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>RM</td>
      <td>35.0</td>
      <td>3675</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>RL</td>
      <td>90.0</td>
      <td>17217</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>FV</td>
      <td>62.0</td>
      <td>7500</td>
      <td>Pave</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>RL</td>
      <td>62.0</td>
      <td>7917</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>RL</td>
      <td>85.0</td>
      <td>13175</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>RL</td>
      <td>66.0</td>
      <td>9042</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>Shed</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>RL</td>
      <td>68.0</td>
      <td>9717</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9937</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 80 columns</p>
</div>




```python
import matplotlib.pyplot as plt
for col in dfcvl:
    if df.dtypes[col] in ['object']:
        plt.figure()
        pd.DataFrame(pd.value_counts(df[col])).plot.bar()
    
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



    <matplotlib.figure.Figure at 0x7fc5ca7e6b70>



![png](output_29_2.png)



    <matplotlib.figure.Figure at 0x7fc5c201d668>



![png](output_29_4.png)



    <matplotlib.figure.Figure at 0x7fc5cafb3f98>



![png](output_29_6.png)



    <matplotlib.figure.Figure at 0x7fc5c1baacc0>



![png](output_29_8.png)



    <matplotlib.figure.Figure at 0x7fc5cafbb390>



![png](output_29_10.png)



    <matplotlib.figure.Figure at 0x7fc5c976b278>



![png](output_29_12.png)



    <matplotlib.figure.Figure at 0x7fc5c29b4ef0>



![png](output_29_14.png)



    <matplotlib.figure.Figure at 0x7fc5c9a9ef60>



![png](output_29_16.png)



    <matplotlib.figure.Figure at 0x7fc5c8136630>



![png](output_29_18.png)



    <matplotlib.figure.Figure at 0x7fc5ca59a9b0>



![png](output_29_20.png)



    <matplotlib.figure.Figure at 0x7fc5ca5aeef0>



![png](output_29_22.png)



    <matplotlib.figure.Figure at 0x7fc5ca33a198>



![png](output_29_24.png)



    <matplotlib.figure.Figure at 0x7fc5ca4542e8>



![png](output_29_26.png)



    <matplotlib.figure.Figure at 0x7fc5cabb2978>



![png](output_29_28.png)



    <matplotlib.figure.Figure at 0x7fc5c128f8d0>



![png](output_29_30.png)



    <matplotlib.figure.Figure at 0x7fc5c380c208>



![png](output_29_32.png)



    <matplotlib.figure.Figure at 0x7fc5cb0f1e80>



![png](output_29_34.png)



    <matplotlib.figure.Figure at 0x7fc5c8c4bc18>



![png](output_29_36.png)



    <matplotlib.figure.Figure at 0x7fc5c2a31c88>



![png](output_29_38.png)



    <matplotlib.figure.Figure at 0x7fc5c2d08fd0>



![png](output_29_40.png)



    <matplotlib.figure.Figure at 0x7fc5c8f51b70>



![png](output_29_42.png)



    <matplotlib.figure.Figure at 0x7fc5c1257278>



![png](output_29_44.png)



    <matplotlib.figure.Figure at 0x7fc5ca582278>



![png](output_29_46.png)



    <matplotlib.figure.Figure at 0x7fc5c913a7f0>



![png](output_29_48.png)



    <matplotlib.figure.Figure at 0x7fc5c887a0b8>



![png](output_29_50.png)



    <matplotlib.figure.Figure at 0x7fc5c8de7828>



![png](output_29_52.png)



    <matplotlib.figure.Figure at 0x7fc5c9efc208>



![png](output_29_54.png)



    <matplotlib.figure.Figure at 0x7fc5c26a0320>



![png](output_29_56.png)



    <matplotlib.figure.Figure at 0x7fc5cb18e240>



![png](output_29_58.png)



    <matplotlib.figure.Figure at 0x7fc5c8e08be0>



![png](output_29_60.png)



    <matplotlib.figure.Figure at 0x7fc5caeee978>



![png](output_29_62.png)



    <matplotlib.figure.Figure at 0x7fc5c9c4c320>



![png](output_29_64.png)



    <matplotlib.figure.Figure at 0x7fc5ca2f33c8>



![png](output_29_66.png)



    <matplotlib.figure.Figure at 0x7fc5c295a390>



![png](output_29_68.png)



    <matplotlib.figure.Figure at 0x7fc5c16abbe0>



![png](output_29_70.png)



    <matplotlib.figure.Figure at 0x7fc5c2548cf8>



![png](output_29_72.png)



    <matplotlib.figure.Figure at 0x7fc5c19b6e10>



![png](output_29_74.png)



    <matplotlib.figure.Figure at 0x7fc5cabb0748>



![png](output_29_76.png)



    <matplotlib.figure.Figure at 0x7fc5c3d18320>



![png](output_29_78.png)



    <matplotlib.figure.Figure at 0x7fc5c155dc18>



![png](output_29_80.png)



    <matplotlib.figure.Figure at 0x7fc5c9ef06a0>



![png](output_29_82.png)



    <matplotlib.figure.Figure at 0x7fc5c9efceb8>



![png](output_29_84.png)



    <matplotlib.figure.Figure at 0x7fc5c82b2e80>



![png](output_29_86.png)



```python
for col in dfcvl:
    if str(df.dtypes[col]) not in ['object']:
        print(col)
```

    MSSubClass
    LotFrontage
    LotArea
    OverallQual
    OverallCond
    YearBuilt
    YearRemodAdd
    MasVnrArea
    BsmtFinSF1
    BsmtFinSF2
    BsmtUnfSF
    TotalBsmtSF
    1stFlrSF
    2ndFlrSF
    LowQualFinSF
    GrLivArea
    BsmtFullBath
    BsmtHalfBath
    FullBath
    HalfBath
    BedroomAbvGr
    KitchenAbvGr
    TotRmsAbvGrd
    Fireplaces
    GarageYrBlt
    GarageCars
    GarageArea
    WoodDeckSF
    OpenPorchSF
    EnclosedPorch
    3SsnPorch
    ScreenPorch
    PoolArea
    MiscVal
    MoSold
    YrSold
    SalePrice



```python
for col in dfcvl:
    if str(df.dtypes[col]) not in ["object"]:
        print(df[col].quantile([.05,.1,.25,.5,.75,.9,.99]))
```

    0.05     20.0
    0.10     20.0
    0.25     20.0
    0.50     50.0
    0.75     70.0
    0.90    120.0
    0.99    190.0
    Name: MSSubClass, dtype: float64
    0.05   NaN
    0.10   NaN
    0.25   NaN
    0.50   NaN
    0.75   NaN
    0.90   NaN
    0.99   NaN
    Name: LotFrontage, dtype: float64
    0.05     3311.70
    0.10     5000.00
    0.25     7553.50
    0.50     9478.50
    0.75    11601.50
    0.90    14381.70
    0.99    37567.64
    Name: LotArea, dtype: float64
    0.05     4.0
    0.10     5.0
    0.25     5.0
    0.50     6.0
    0.75     7.0
    0.90     8.0
    0.99    10.0
    Name: OverallQual, dtype: float64
    0.05    4.0
    0.10    5.0
    0.25    5.0
    0.50    5.0
    0.75    6.0
    0.90    7.0
    0.99    9.0
    Name: OverallCond, dtype: float64
    0.05    1916.0
    0.10    1924.9
    0.25    1954.0
    0.50    1973.0
    0.75    2000.0
    0.90    2006.0
    0.99    2009.0
    Name: YearBuilt, dtype: float64
    0.05    1950.0
    0.10    1950.0
    0.25    1967.0
    0.50    1994.0
    0.75    2004.0
    0.90    2006.0
    0.99    2009.0
    Name: YearRemodAdd, dtype: float64
    0.05   NaN
    0.10   NaN
    0.25   NaN
    0.50   NaN
    0.75   NaN
    0.90   NaN
    0.99   NaN
    Name: MasVnrArea, dtype: float64
    0.05       0.00
    0.10       0.00
    0.25       0.00
    0.50     383.50
    0.75     712.25
    0.90    1065.50
    0.99    1572.41
    Name: BsmtFinSF1, dtype: float64
    0.05      0.00
    0.10      0.00
    0.25      0.00
    0.50      0.00
    0.75      0.00
    0.90    117.20
    0.99    830.38
    Name: BsmtFinSF2, dtype: float64
    0.05       0.00
    0.10      74.90
    0.25     223.00
    0.50     477.50
    0.75     808.00
    0.90    1232.00
    0.99    1797.05
    Name: BsmtUnfSF, dtype: float64
    0.05     519.30
    0.10     636.90
    0.25     795.75
    0.50     991.50
    0.75    1298.25
    0.90    1602.20
    0.99    2155.05
    Name: TotalBsmtSF, dtype: float64
    0.05     672.95
    0.10     756.90
    0.25     882.00
    0.50    1087.00
    0.75    1391.25
    0.90    1680.00
    0.99    2219.46
    Name: 1stFlrSF, dtype: float64
    0.05       0.00
    0.10       0.00
    0.25       0.00
    0.50       0.00
    0.75     728.00
    0.90     954.20
    0.99    1418.92
    Name: 2ndFlrSF, dtype: float64
    0.05      0.0
    0.10      0.0
    0.25      0.0
    0.50      0.0
    0.75      0.0
    0.90      0.0
    0.99    360.0
    Name: LowQualFinSF, dtype: float64
    0.05     848.00
    0.10     912.00
    0.25    1129.50
    0.50    1464.00
    0.75    1776.75
    0.90    2158.30
    0.99    3123.48
    Name: GrLivArea, dtype: float64
    0.05    0.0
    0.10    0.0
    0.25    0.0
    0.50    0.0
    0.75    1.0
    0.90    1.0
    0.99    2.0
    Name: BsmtFullBath, dtype: float64
    0.05    0.0
    0.10    0.0
    0.25    0.0
    0.50    0.0
    0.75    0.0
    0.90    0.0
    0.99    1.0
    Name: BsmtHalfBath, dtype: float64
    0.05    1.0
    0.10    1.0
    0.25    1.0
    0.50    2.0
    0.75    2.0
    0.90    2.0
    0.99    3.0
    Name: FullBath, dtype: float64
    0.05    0.0
    0.10    0.0
    0.25    0.0
    0.50    0.0
    0.75    1.0
    0.90    1.0
    0.99    1.0
    Name: HalfBath, dtype: float64
    0.05    2.0
    0.10    2.0
    0.25    2.0
    0.50    3.0
    0.75    3.0
    0.90    4.0
    0.99    5.0
    Name: BedroomAbvGr, dtype: float64
    0.05    1.0
    0.10    1.0
    0.25    1.0
    0.50    1.0
    0.75    1.0
    0.90    1.0
    0.99    2.0
    Name: KitchenAbvGr, dtype: float64
    0.05     4.0
    0.10     5.0
    0.25     5.0
    0.50     6.0
    0.75     7.0
    0.90     9.0
    0.99    11.0
    Name: TotRmsAbvGrd, dtype: float64
    0.05    0.0
    0.10    0.0
    0.25    0.0
    0.50    1.0
    0.75    1.0
    0.90    1.0
    0.99    2.0
    Name: Fireplaces, dtype: float64
    0.05   NaN
    0.10   NaN
    0.25   NaN
    0.50   NaN
    0.75   NaN
    0.90   NaN
    0.99   NaN
    Name: GarageYrBlt, dtype: float64
    0.05    0.0
    0.10    1.0
    0.25    1.0
    0.50    2.0
    0.75    2.0
    0.90    3.0
    0.99    3.0
    Name: GarageCars, dtype: float64
    0.05       0.00
    0.10     240.00
    0.25     334.50
    0.50     480.00
    0.75     576.00
    0.90     757.10
    0.99    1002.79
    Name: GarageArea, dtype: float64
    0.05      0.00
    0.10      0.00
    0.25      0.00
    0.50      0.00
    0.75    168.00
    0.90    262.00
    0.99    505.46
    Name: WoodDeckSF, dtype: float64
    0.05      0.00
    0.10      0.00
    0.25      0.00
    0.50     25.00
    0.75     68.00
    0.90    130.00
    0.99    285.82
    Name: OpenPorchSF, dtype: float64
    0.05      0.00
    0.10      0.00
    0.25      0.00
    0.50      0.00
    0.75      0.00
    0.90    112.00
    0.99    261.05
    Name: EnclosedPorch, dtype: float64
    0.05      0.0
    0.10      0.0
    0.25      0.0
    0.50      0.0
    0.75      0.0
    0.90      0.0
    0.99    168.0
    Name: 3SsnPorch, dtype: float64
    0.05      0.00
    0.10      0.00
    0.25      0.00
    0.50      0.00
    0.75      0.00
    0.90      0.00
    0.99    268.05
    Name: ScreenPorch, dtype: float64
    0.05    0.0
    0.10    0.0
    0.25    0.0
    0.50    0.0
    0.75    0.0
    0.90    0.0
    0.99    0.0
    Name: PoolArea, dtype: float64
    0.05      0.0
    0.10      0.0
    0.25      0.0
    0.50      0.0
    0.75      0.0
    0.90      0.0
    0.99    700.0
    Name: MiscVal, dtype: float64
    0.05     2.0
    0.10     3.0
    0.25     5.0
    0.50     6.0
    0.75     8.0
    0.90    10.0
    0.99    12.0
    Name: MoSold, dtype: float64
    0.05    2006.0
    0.10    2006.0
    0.25    2007.0
    0.50    2008.0
    0.75    2009.0
    0.90    2010.0
    0.99    2010.0
    Name: YrSold, dtype: float64
    0.05     88000.00
    0.10    106475.00
    0.25    129975.00
    0.50    163000.00
    0.75    214000.00
    0.90    278000.00
    0.99    442567.01
    Name: SalePrice, dtype: float64


    /usr/local/lib/python3.5/dist-packages/numpy/lib/function_base.py:3834: RuntimeWarning: Invalid value encountered in percentile
      RuntimeWarning)



```python

```


```python
for col in dfcvl:
    if str(df.dtypes[col]) not in ["object"]:
        plt.figure()
        plt.title(col)
        df[col].plot.hist()
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



![png](output_33_1.png)



![png](output_33_2.png)



![png](output_33_3.png)



![png](output_33_4.png)



![png](output_33_5.png)



![png](output_33_6.png)



![png](output_33_7.png)



![png](output_33_8.png)



![png](output_33_9.png)



![png](output_33_10.png)



![png](output_33_11.png)



![png](output_33_12.png)



![png](output_33_13.png)



![png](output_33_14.png)



![png](output_33_15.png)



![png](output_33_16.png)



![png](output_33_17.png)



![png](output_33_18.png)



![png](output_33_19.png)



![png](output_33_20.png)



![png](output_33_21.png)



![png](output_33_22.png)



![png](output_33_23.png)



![png](output_33_24.png)



![png](output_33_25.png)



![png](output_33_26.png)



![png](output_33_27.png)



![png](output_33_28.png)



![png](output_33_29.png)



![png](output_33_30.png)



![png](output_33_31.png)



![png](output_33_32.png)



![png](output_33_33.png)



![png](output_33_34.png)



![png](output_33_35.png)



![png](output_33_36.png)



![png](output_33_37.png)



```python
for col in dfcvl:
    if str(df.dtypes[col]) not in ["object"]:
        plt.figure()
        plt.title(col)
        df[col].plot.hist(normed=True)
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



![png](output_34_1.png)



![png](output_34_2.png)



![png](output_34_3.png)



![png](output_34_4.png)



![png](output_34_5.png)



![png](output_34_6.png)



![png](output_34_7.png)



![png](output_34_8.png)



![png](output_34_9.png)



![png](output_34_10.png)



![png](output_34_11.png)



![png](output_34_12.png)



![png](output_34_13.png)



![png](output_34_14.png)



![png](output_34_15.png)



![png](output_34_16.png)



![png](output_34_17.png)



![png](output_34_18.png)



![png](output_34_19.png)



![png](output_34_20.png)



![png](output_34_21.png)



![png](output_34_22.png)



![png](output_34_23.png)



![png](output_34_24.png)



![png](output_34_25.png)



![png](output_34_26.png)



![png](output_34_27.png)



![png](output_34_28.png)



![png](output_34_29.png)



![png](output_34_30.png)



![png](output_34_31.png)



![png](output_34_32.png)



![png](output_34_33.png)



![png](output_34_34.png)



![png](output_34_35.png)



![png](output_34_36.png)



![png](output_34_37.png)


`Note: dtype <conditional operator> '<dtype>' - works , where as dtype <conditional operator) "<dtype>"`


```python
for col in dfcvl:
    if str(df.dtypes[col]) not in ["object"]:
        plt.figure()
        plt.title(col)
        df[col].plot.hist(normed=True, cumulative=True)
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



![png](output_36_1.png)



![png](output_36_2.png)



![png](output_36_3.png)



![png](output_36_4.png)



![png](output_36_5.png)



![png](output_36_6.png)



![png](output_36_7.png)



![png](output_36_8.png)



![png](output_36_9.png)



![png](output_36_10.png)



![png](output_36_11.png)



![png](output_36_12.png)



![png](output_36_13.png)



![png](output_36_14.png)



![png](output_36_15.png)



![png](output_36_16.png)



![png](output_36_17.png)



![png](output_36_18.png)



![png](output_36_19.png)



![png](output_36_20.png)



![png](output_36_21.png)



![png](output_36_22.png)



![png](output_36_23.png)



![png](output_36_24.png)



![png](output_36_25.png)



![png](output_36_26.png)



![png](output_36_27.png)



![png](output_36_28.png)



![png](output_36_29.png)



![png](output_36_30.png)



![png](output_36_31.png)



![png](output_36_32.png)



![png](output_36_33.png)



![png](output_36_34.png)



![png](output_36_35.png)



![png](output_36_36.png)



![png](output_36_37.png)



```python
for col in dfcvl:
    if str(df.dtypes[col]) not in ["object"]:
        plt.figure()
        plt.title(col)
        df[col].plot.hist( histtype="step")
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



![png](output_37_1.png)



![png](output_37_2.png)



![png](output_37_3.png)



![png](output_37_4.png)



![png](output_37_5.png)



![png](output_37_6.png)



![png](output_37_7.png)



![png](output_37_8.png)



![png](output_37_9.png)



![png](output_37_10.png)



![png](output_37_11.png)



![png](output_37_12.png)



![png](output_37_13.png)



![png](output_37_14.png)



![png](output_37_15.png)



![png](output_37_16.png)



![png](output_37_17.png)



![png](output_37_18.png)



![png](output_37_19.png)



![png](output_37_20.png)



![png](output_37_21.png)



![png](output_37_22.png)



![png](output_37_23.png)



![png](output_37_24.png)



![png](output_37_25.png)



![png](output_37_26.png)



![png](output_37_27.png)



![png](output_37_28.png)



![png](output_37_29.png)



![png](output_37_30.png)



![png](output_37_31.png)



![png](output_37_32.png)



![png](output_37_33.png)



![png](output_37_34.png)



![png](output_37_35.png)



![png](output_37_36.png)



![png](output_37_37.png)



```python
for col in dfcvl:
    if df.dtypes[col] not in ['object']:
        plt.figure()
        plt.title(col)
        df[col].plot.box()
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



![png](output_38_1.png)



![png](output_38_2.png)



![png](output_38_3.png)



![png](output_38_4.png)



![png](output_38_5.png)



![png](output_38_6.png)



![png](output_38_7.png)



![png](output_38_8.png)



![png](output_38_9.png)



![png](output_38_10.png)



![png](output_38_11.png)



![png](output_38_12.png)



![png](output_38_13.png)



![png](output_38_14.png)



![png](output_38_15.png)



![png](output_38_16.png)



![png](output_38_17.png)



![png](output_38_18.png)



![png](output_38_19.png)



![png](output_38_20.png)



![png](output_38_21.png)



![png](output_38_22.png)



![png](output_38_23.png)



![png](output_38_24.png)



![png](output_38_25.png)



![png](output_38_26.png)



![png](output_38_27.png)



![png](output_38_28.png)



![png](output_38_29.png)



![png](output_38_30.png)



![png](output_38_31.png)



![png](output_38_32.png)



![png](output_38_33.png)



![png](output_38_34.png)



![png](output_38_35.png)



![png](output_38_36.png)



![png](output_38_37.png)



```python
dfcont=df.filter(items=filter(lambda col: df.dtypes[col] not in ['object'],dfcvl))
dfcont
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>OverallQual</th>
      <th>OverallCond</th>
      <th>YearBuilt</th>
      <th>YearRemodAdd</th>
      <th>MasVnrArea</th>
      <th>BsmtFinSF1</th>
      <th>BsmtFinSF2</th>
      <th>...</th>
      <th>WoodDeckSF</th>
      <th>OpenPorchSF</th>
      <th>EnclosedPorch</th>
      <th>3SsnPorch</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>65.0</td>
      <td>8450</td>
      <td>7</td>
      <td>5</td>
      <td>2003</td>
      <td>2003</td>
      <td>196.0</td>
      <td>706</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>61</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>80.0</td>
      <td>9600</td>
      <td>6</td>
      <td>8</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>978</td>
      <td>0</td>
      <td>...</td>
      <td>298</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>68.0</td>
      <td>11250</td>
      <td>7</td>
      <td>5</td>
      <td>2001</td>
      <td>2002</td>
      <td>162.0</td>
      <td>486</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>60.0</td>
      <td>9550</td>
      <td>7</td>
      <td>5</td>
      <td>1915</td>
      <td>1970</td>
      <td>0.0</td>
      <td>216</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>35</td>
      <td>272</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>84.0</td>
      <td>14260</td>
      <td>8</td>
      <td>5</td>
      <td>2000</td>
      <td>2000</td>
      <td>350.0</td>
      <td>655</td>
      <td>0</td>
      <td>...</td>
      <td>192</td>
      <td>84</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>85.0</td>
      <td>14115</td>
      <td>5</td>
      <td>5</td>
      <td>1993</td>
      <td>1995</td>
      <td>0.0</td>
      <td>732</td>
      <td>0</td>
      <td>...</td>
      <td>40</td>
      <td>30</td>
      <td>0</td>
      <td>320</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>75.0</td>
      <td>10084</td>
      <td>8</td>
      <td>5</td>
      <td>2004</td>
      <td>2005</td>
      <td>186.0</td>
      <td>1369</td>
      <td>0</td>
      <td>...</td>
      <td>255</td>
      <td>57</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>NaN</td>
      <td>10382</td>
      <td>7</td>
      <td>6</td>
      <td>1973</td>
      <td>1973</td>
      <td>240.0</td>
      <td>859</td>
      <td>32</td>
      <td>...</td>
      <td>235</td>
      <td>204</td>
      <td>228</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>51.0</td>
      <td>6120</td>
      <td>7</td>
      <td>5</td>
      <td>1931</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>90</td>
      <td>0</td>
      <td>205</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>50.0</td>
      <td>7420</td>
      <td>5</td>
      <td>6</td>
      <td>1939</td>
      <td>1950</td>
      <td>0.0</td>
      <td>851</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>70.0</td>
      <td>11200</td>
      <td>5</td>
      <td>5</td>
      <td>1965</td>
      <td>1965</td>
      <td>0.0</td>
      <td>906</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>85.0</td>
      <td>11924</td>
      <td>9</td>
      <td>5</td>
      <td>2005</td>
      <td>2006</td>
      <td>286.0</td>
      <td>998</td>
      <td>0</td>
      <td>...</td>
      <td>147</td>
      <td>21</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>NaN</td>
      <td>12968</td>
      <td>5</td>
      <td>6</td>
      <td>1962</td>
      <td>1962</td>
      <td>0.0</td>
      <td>737</td>
      <td>0</td>
      <td>...</td>
      <td>140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>176</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>91.0</td>
      <td>10652</td>
      <td>7</td>
      <td>5</td>
      <td>2006</td>
      <td>2007</td>
      <td>306.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>160</td>
      <td>33</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>NaN</td>
      <td>10920</td>
      <td>6</td>
      <td>5</td>
      <td>1960</td>
      <td>1960</td>
      <td>212.0</td>
      <td>733</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>213</td>
      <td>176</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>51.0</td>
      <td>6120</td>
      <td>7</td>
      <td>8</td>
      <td>1929</td>
      <td>2001</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>48</td>
      <td>112</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>NaN</td>
      <td>11241</td>
      <td>6</td>
      <td>7</td>
      <td>1970</td>
      <td>1970</td>
      <td>180.0</td>
      <td>578</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>72.0</td>
      <td>10791</td>
      <td>4</td>
      <td>5</td>
      <td>1967</td>
      <td>1967</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>66.0</td>
      <td>13695</td>
      <td>5</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>0.0</td>
      <td>646</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>102</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>70.0</td>
      <td>7560</td>
      <td>5</td>
      <td>6</td>
      <td>1958</td>
      <td>1965</td>
      <td>0.0</td>
      <td>504</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>101.0</td>
      <td>14215</td>
      <td>8</td>
      <td>5</td>
      <td>2005</td>
      <td>2006</td>
      <td>380.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>240</td>
      <td>154</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>57.0</td>
      <td>7449</td>
      <td>7</td>
      <td>7</td>
      <td>1930</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>205</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>75.0</td>
      <td>9742</td>
      <td>8</td>
      <td>5</td>
      <td>2002</td>
      <td>2002</td>
      <td>281.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>171</td>
      <td>159</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>44.0</td>
      <td>4224</td>
      <td>5</td>
      <td>7</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>840</td>
      <td>0</td>
      <td>...</td>
      <td>100</td>
      <td>110</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>NaN</td>
      <td>8246</td>
      <td>5</td>
      <td>8</td>
      <td>1968</td>
      <td>2001</td>
      <td>0.0</td>
      <td>188</td>
      <td>668</td>
      <td>...</td>
      <td>406</td>
      <td>90</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>110.0</td>
      <td>14230</td>
      <td>8</td>
      <td>5</td>
      <td>2007</td>
      <td>2007</td>
      <td>640.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>56</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>60.0</td>
      <td>7200</td>
      <td>5</td>
      <td>7</td>
      <td>1951</td>
      <td>2000</td>
      <td>0.0</td>
      <td>234</td>
      <td>486</td>
      <td>...</td>
      <td>222</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>98.0</td>
      <td>11478</td>
      <td>8</td>
      <td>5</td>
      <td>2007</td>
      <td>2008</td>
      <td>200.0</td>
      <td>1218</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>47.0</td>
      <td>16321</td>
      <td>5</td>
      <td>6</td>
      <td>1957</td>
      <td>1997</td>
      <td>0.0</td>
      <td>1277</td>
      <td>0</td>
      <td>...</td>
      <td>288</td>
      <td>258</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>60.0</td>
      <td>6324</td>
      <td>4</td>
      <td>6</td>
      <td>1927</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>49</td>
      <td>0</td>
      <td>87</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>60.0</td>
      <td>21930</td>
      <td>5</td>
      <td>5</td>
      <td>2005</td>
      <td>2005</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>100</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>NaN</td>
      <td>4928</td>
      <td>6</td>
      <td>6</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>958</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>60.0</td>
      <td>10800</td>
      <td>4</td>
      <td>6</td>
      <td>1927</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>93.0</td>
      <td>10261</td>
      <td>6</td>
      <td>5</td>
      <td>2000</td>
      <td>2000</td>
      <td>318.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>80.0</td>
      <td>17400</td>
      <td>5</td>
      <td>5</td>
      <td>1977</td>
      <td>1977</td>
      <td>0.0</td>
      <td>936</td>
      <td>0</td>
      <td>...</td>
      <td>295</td>
      <td>41</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>80.0</td>
      <td>8400</td>
      <td>6</td>
      <td>9</td>
      <td>1962</td>
      <td>2005</td>
      <td>237.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>60.0</td>
      <td>9000</td>
      <td>4</td>
      <td>6</td>
      <td>1971</td>
      <td>1971</td>
      <td>0.0</td>
      <td>616</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>96.0</td>
      <td>12444</td>
      <td>8</td>
      <td>5</td>
      <td>2008</td>
      <td>2008</td>
      <td>426.0</td>
      <td>1336</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>66</td>
      <td>0</td>
      <td>304</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>90.0</td>
      <td>7407</td>
      <td>6</td>
      <td>7</td>
      <td>1957</td>
      <td>1996</td>
      <td>0.0</td>
      <td>600</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>158</td>
      <td>158</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>80.0</td>
      <td>11584</td>
      <td>7</td>
      <td>6</td>
      <td>1979</td>
      <td>1979</td>
      <td>96.0</td>
      <td>315</td>
      <td>110</td>
      <td>...</td>
      <td>0</td>
      <td>88</td>
      <td>216</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>79.0</td>
      <td>11526</td>
      <td>6</td>
      <td>7</td>
      <td>1922</td>
      <td>1994</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>431</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>NaN</td>
      <td>4426</td>
      <td>6</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>147.0</td>
      <td>697</td>
      <td>0</td>
      <td>...</td>
      <td>149</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>85.0</td>
      <td>11003</td>
      <td>10</td>
      <td>5</td>
      <td>2008</td>
      <td>2008</td>
      <td>160.0</td>
      <td>765</td>
      <td>0</td>
      <td>...</td>
      <td>168</td>
      <td>52</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>NaN</td>
      <td>8854</td>
      <td>6</td>
      <td>6</td>
      <td>1916</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>98</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>63.0</td>
      <td>8500</td>
      <td>7</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>106.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>192</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>70.0</td>
      <td>8400</td>
      <td>6</td>
      <td>5</td>
      <td>1966</td>
      <td>1966</td>
      <td>0.0</td>
      <td>187</td>
      <td>627</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>252</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>NaN</td>
      <td>26142</td>
      <td>5</td>
      <td>7</td>
      <td>1962</td>
      <td>1962</td>
      <td>189.0</td>
      <td>593</td>
      <td>0</td>
      <td>...</td>
      <td>261</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>80.0</td>
      <td>10000</td>
      <td>8</td>
      <td>5</td>
      <td>1995</td>
      <td>1996</td>
      <td>438.0</td>
      <td>1079</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>65</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>70.0</td>
      <td>11767</td>
      <td>4</td>
      <td>7</td>
      <td>1910</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>168</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>21.0</td>
      <td>1533</td>
      <td>5</td>
      <td>7</td>
      <td>1970</td>
      <td>1970</td>
      <td>0.0</td>
      <td>553</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>60.0</td>
      <td>9000</td>
      <td>5</td>
      <td>5</td>
      <td>1974</td>
      <td>1974</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>32</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>78.0</td>
      <td>9262</td>
      <td>8</td>
      <td>5</td>
      <td>2008</td>
      <td>2009</td>
      <td>194.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>35.0</td>
      <td>3675</td>
      <td>5</td>
      <td>5</td>
      <td>2005</td>
      <td>2005</td>
      <td>80.0</td>
      <td>547</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>90.0</td>
      <td>17217</td>
      <td>5</td>
      <td>5</td>
      <td>2006</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>36</td>
      <td>56</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>62.0</td>
      <td>7500</td>
      <td>7</td>
      <td>5</td>
      <td>2004</td>
      <td>2005</td>
      <td>0.0</td>
      <td>410</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>113</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>62.0</td>
      <td>7917</td>
      <td>6</td>
      <td>5</td>
      <td>1999</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>85.0</td>
      <td>13175</td>
      <td>6</td>
      <td>6</td>
      <td>1978</td>
      <td>1988</td>
      <td>119.0</td>
      <td>790</td>
      <td>163</td>
      <td>...</td>
      <td>349</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>66.0</td>
      <td>9042</td>
      <td>7</td>
      <td>9</td>
      <td>1941</td>
      <td>2006</td>
      <td>0.0</td>
      <td>275</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>68.0</td>
      <td>9717</td>
      <td>5</td>
      <td>6</td>
      <td>1950</td>
      <td>1996</td>
      <td>0.0</td>
      <td>49</td>
      <td>1029</td>
      <td>...</td>
      <td>366</td>
      <td>0</td>
      <td>112</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>75.0</td>
      <td>9937</td>
      <td>5</td>
      <td>6</td>
      <td>1965</td>
      <td>1965</td>
      <td>0.0</td>
      <td>830</td>
      <td>290</td>
      <td>...</td>
      <td>736</td>
      <td>68</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 37 columns</p>
</div>




```python
dfcat=df.filter(items=filter(lambda col: df.dtypes[col]  in ['object'],dfcvl))
dfcat
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSZoning</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>LandSlope</th>
      <th>Neighborhood</th>
      <th>Condition1</th>
      <th>...</th>
      <th>GarageType</th>
      <th>GarageFinish</th>
      <th>GarageQual</th>
      <th>GarageCond</th>
      <th>PavedDrive</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>Gtl</td>
      <td>Veenker</td>
      <td>Feedr</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>Crawfor</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>Gtl</td>
      <td>NoRidge</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>Shed</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>6</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Somerst</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NWAmes</td>
      <td>PosN</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>OldTown</td>
      <td>Artery</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>Fa</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>9</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>BrkSide</td>
      <td>Artery</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>Gd</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>10</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Sawyer</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>11</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NridgHt</td>
      <td>Norm</td>
      <td>...</td>
      <td>BuiltIn</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>New</td>
      <td>Partial</td>
    </tr>
    <tr>
      <th>12</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR2</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Sawyer</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>13</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>New</td>
      <td>Partial</td>
    </tr>
    <tr>
      <th>14</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>15</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>BrkSide</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>16</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>17</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Sawyer</td>
      <td>Norm</td>
      <td>...</td>
      <td>CarPort</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>18</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>SawyerW</td>
      <td>RRAe</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>19</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>COD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>20</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NridgHt</td>
      <td>Norm</td>
      <td>...</td>
      <td>BuiltIn</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>New</td>
      <td>Partial</td>
    </tr>
    <tr>
      <th>21</th>
      <td>RM</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>IDOTRR</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>N</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>22</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>23</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>MeadowV</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>24</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Sawyer</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>25</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NridgHt</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>26</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>27</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NridgHt</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>28</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>29</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>BrkSide</td>
      <td>Feedr</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>Fa</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR3</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Gilbert</td>
      <td>RRAn</td>
      <td>...</td>
      <td>BuiltIn</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NPkVill</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>RL</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>OldTown</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>Fa</td>
      <td>Fa</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Gilbert</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>P</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>COD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>Gtl</td>
      <td>NridgHt</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>New</td>
      <td>Partial</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>OldTown</td>
      <td>Artery</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NWAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Crawfor</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>FV</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Somerst</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>BrkSide</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>Fa</td>
      <td>Po</td>
      <td>P</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Sawyer</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>P</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>CollgCr</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Edwards</td>
      <td>Norm</td>
      <td>...</td>
      <td>Detchd</td>
      <td>Unf</td>
      <td>Fa</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>MeadowV</td>
      <td>Norm</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Somerst</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>New</td>
      <td>Partial</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>RM</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Edwards</td>
      <td>Norm</td>
      <td>...</td>
      <td>Basment</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>FV</td>
      <td>Pave</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Somerst</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Gilbert</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NWAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Crawfor</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>RFn</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>Shed</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Unf</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>RL</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Edwards</td>
      <td>Norm</td>
      <td>...</td>
      <td>Attchd</td>
      <td>Fin</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 43 columns</p>
</div>




```python
catcols=[]
contcols=[]
for col in dfcvl:
    cols = catcols if df[col].dtype == 'O' else contcols
    cols.append(col)
catcols,contcols
```




    (['MSZoning',
      'Street',
      'Alley',
      'LotShape',
      'LandContour',
      'Utilities',
      'LotConfig',
      'LandSlope',
      'Neighborhood',
      'Condition1',
      'Condition2',
      'BldgType',
      'HouseStyle',
      'RoofStyle',
      'RoofMatl',
      'Exterior1st',
      'Exterior2nd',
      'MasVnrType',
      'ExterQual',
      'ExterCond',
      'Foundation',
      'BsmtQual',
      'BsmtCond',
      'BsmtExposure',
      'BsmtFinType1',
      'BsmtFinType2',
      'Heating',
      'HeatingQC',
      'CentralAir',
      'Electrical',
      'KitchenQual',
      'Functional',
      'FireplaceQu',
      'GarageType',
      'GarageFinish',
      'GarageQual',
      'GarageCond',
      'PavedDrive',
      'PoolQC',
      'Fence',
      'MiscFeature',
      'SaleType',
      'SaleCondition'],
     ['MSSubClass',
      'LotFrontage',
      'LotArea',
      'OverallQual',
      'OverallCond',
      'YearBuilt',
      'YearRemodAdd',
      'MasVnrArea',
      'BsmtFinSF1',
      'BsmtFinSF2',
      'BsmtUnfSF',
      'TotalBsmtSF',
      '1stFlrSF',
      '2ndFlrSF',
      'LowQualFinSF',
      'GrLivArea',
      'BsmtFullBath',
      'BsmtHalfBath',
      'FullBath',
      'HalfBath',
      'BedroomAbvGr',
      'KitchenAbvGr',
      'TotRmsAbvGrd',
      'Fireplaces',
      'GarageYrBlt',
      'GarageCars',
      'GarageArea',
      'WoodDeckSF',
      'OpenPorchSF',
      'EnclosedPorch',
      '3SsnPorch',
      'ScreenPorch',
      'PoolArea',
      'MiscVal',
      'MoSold',
      'YrSold',
      'SalePrice'])




```python
dfwtcatencode=pd.DataFrame()
for col in df.columns:
    if col in dfcat.columns:
        dfwtcatencode[col]=df[col].astype("category").cat.codes
    else:
        dfwtcatencode[col]=df[col]
dfwtcatencode
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>3</td>
      <td>65.0</td>
      <td>8450</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>9600</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>3</td>
      <td>68.0</td>
      <td>11250</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>3</td>
      <td>60.0</td>
      <td>9550</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>3</td>
      <td>84.0</td>
      <td>14260</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>3</td>
      <td>85.0</td>
      <td>14115</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>2</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>10084</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>3</td>
      <td>NaN</td>
      <td>10382</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>4</td>
      <td>51.0</td>
      <td>6120</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>8</td>
      <td>0</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>3</td>
      <td>50.0</td>
      <td>7420</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>3</td>
      <td>70.0</td>
      <td>11200</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>3</td>
      <td>85.0</td>
      <td>11924</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>6</td>
      <td>5</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>3</td>
      <td>NaN</td>
      <td>12968</td>
      <td>1</td>
      <td>-1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>3</td>
      <td>91.0</td>
      <td>10652</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>6</td>
      <td>5</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>3</td>
      <td>NaN</td>
      <td>10920</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>4</td>
      <td>51.0</td>
      <td>6120</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>3</td>
      <td>NaN</td>
      <td>11241</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>3</td>
      <td>72.0</td>
      <td>10791</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>3</td>
      <td>66.0</td>
      <td>13695</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>3</td>
      <td>70.0</td>
      <td>7560</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>0</td>
      <td>0</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>3</td>
      <td>101.0</td>
      <td>14215</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>6</td>
      <td>5</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>4</td>
      <td>57.0</td>
      <td>7449</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>9742</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>4</td>
      <td>44.0</td>
      <td>4224</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>3</td>
      <td>NaN</td>
      <td>8246</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>3</td>
      <td>110.0</td>
      <td>14230</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>3</td>
      <td>60.0</td>
      <td>7200</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>3</td>
      <td>98.0</td>
      <td>11478</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>3</td>
      <td>47.0</td>
      <td>16321</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>4</td>
      <td>60.0</td>
      <td>6324</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>3</td>
      <td>60.0</td>
      <td>21930</td>
      <td>1</td>
      <td>-1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>3</td>
      <td>NaN</td>
      <td>4928</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>3</td>
      <td>60.0</td>
      <td>10800</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>3</td>
      <td>93.0</td>
      <td>10261</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>17400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>8400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>0</td>
      <td>0</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>3</td>
      <td>60.0</td>
      <td>9000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>3</td>
      <td>96.0</td>
      <td>12444</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>6</td>
      <td>5</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>4</td>
      <td>90.0</td>
      <td>7407</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>3</td>
      <td>80.0</td>
      <td>11584</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>3</td>
      <td>79.0</td>
      <td>11526</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>4</td>
      <td>NaN</td>
      <td>4426</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>1</td>
      <td>85.0</td>
      <td>11003</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>3</td>
      <td>NaN</td>
      <td>8854</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>3</td>
      <td>63.0</td>
      <td>8500</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>3</td>
      <td>70.0</td>
      <td>8400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>3</td>
      <td>NaN</td>
      <td>26142</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>3</td>
      <td>80.0</td>
      <td>10000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>3</td>
      <td>70.0</td>
      <td>11767</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>4</td>
      <td>21.0</td>
      <td>1533</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>3</td>
      <td>60.0</td>
      <td>9000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>3</td>
      <td>78.0</td>
      <td>9262</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>6</td>
      <td>5</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>4</td>
      <td>35.0</td>
      <td>3675</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>3</td>
      <td>90.0</td>
      <td>17217</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>1</td>
      <td>62.0</td>
      <td>7500</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>3</td>
      <td>62.0</td>
      <td>7917</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>3</td>
      <td>85.0</td>
      <td>13175</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>3</td>
      <td>66.0</td>
      <td>9042</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>3</td>
      <td>68.0</td>
      <td>9717</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>9937</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 80 columns</p>
</div>




```python
dfwtcatencodeagmdcorr=dfwtcatencode.corr().loc[mdcolsl, :]
#[mdcorrcont.isin([1,-1])].dropna(axis=[0,1],how='all').transpose()
dfwtcatencodeagmdcorr=dfwtcatencodeagmdcorr[ ((dfwtcatencodeagmdcorr < -0.5) | (dfwtcatencodeagmdcorr > 0.5))  ]
for col in mdcolsl:
    dfwtcatencodeagmdcorr.loc[col,col]=None
dfwtcatencodeagmdcorr.dropna(axis=[0,1],how='all')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OverallQual</th>
      <th>YearBuilt</th>
      <th>YearRemodAdd</th>
      <th>ExterQual</th>
      <th>Foundation</th>
      <th>BsmtFinSF2</th>
      <th>BsmtUnfSF</th>
      <th>Fireplaces</th>
      <th>GarageType</th>
      <th>GarageYrBlt</th>
      <th>GarageFinish</th>
      <th>GarageCars</th>
      <th>GarageArea</th>
      <th>GarageQual</th>
      <th>GarageCond</th>
      <th>PoolArea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BsmtFinType1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.547581</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>BsmtFinType2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.502744</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>FireplaceQu</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.824059</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageType</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.583956</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>0.547766</td>
      <td>0.825667</td>
      <td>0.642277</td>
      <td>-0.523642</td>
      <td>0.591845</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.525408</td>
      <td>0.588920</td>
      <td>0.564567</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageFinish</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.583956</td>
      <td>-0.525408</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageQual</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.564018</td>
      <td>0.534253</td>
      <td>NaN</td>
      <td>0.902991</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>GarageCond</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.564880</td>
      <td>0.534305</td>
      <td>0.902991</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>PoolQC</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.938402</td>
    </tr>
  </tbody>
</table>
</div>



* Fireplace quality is missing for all number of fireplaces is 0.
* Most cases the garage would be built around same year the house is built, and built during the remoding, or there is no garage for the house.
* For
* PoolQC is missing for house with no Pools of pool Area is zero.

Other values are not correlated with any other values for simplicity I am *assuming* `dangerous with caution`  , min or mean for continuous values and mode for categorical values.


```python
class DataFrameWrapper(object):
    
    def __init__(self,df):
        self.df=df
        
        # Types of columns
        self.continous_columns=[]
        self.categorical_columns=[]

class RawDataSet(object):
    def __init__(self, url):
        self.df = 
    
    def performDataQualityCheck(self):
        return DataQualityReport()
    

class DataQualityReport(object):
    def __init__(self):
        pass
    
        
```


```python
df["LotFrontage"]=dfwtcatencode["LotFrontage"]=dfwtcatencode["LotFrontage"].fillna(0)
dfwtcatencode
#dfwtcatencode["LotFrontage"].plot.box()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>3</td>
      <td>65.0</td>
      <td>8450</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>9600</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>3</td>
      <td>68.0</td>
      <td>11250</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>3</td>
      <td>60.0</td>
      <td>9550</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>3</td>
      <td>84.0</td>
      <td>14260</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>3</td>
      <td>85.0</td>
      <td>14115</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>2</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>10084</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>3</td>
      <td>0.0</td>
      <td>10382</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>4</td>
      <td>51.0</td>
      <td>6120</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>8</td>
      <td>0</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>3</td>
      <td>50.0</td>
      <td>7420</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>3</td>
      <td>70.0</td>
      <td>11200</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>3</td>
      <td>85.0</td>
      <td>11924</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>6</td>
      <td>5</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>12968</td>
      <td>1</td>
      <td>-1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>3</td>
      <td>91.0</td>
      <td>10652</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>6</td>
      <td>5</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>10920</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>4</td>
      <td>51.0</td>
      <td>6120</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>11241</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>3</td>
      <td>72.0</td>
      <td>10791</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>3</td>
      <td>66.0</td>
      <td>13695</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>3</td>
      <td>70.0</td>
      <td>7560</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>0</td>
      <td>0</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>3</td>
      <td>101.0</td>
      <td>14215</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>6</td>
      <td>5</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>4</td>
      <td>57.0</td>
      <td>7449</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>9742</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>4</td>
      <td>44.0</td>
      <td>4224</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>8246</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>3</td>
      <td>110.0</td>
      <td>14230</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>3</td>
      <td>60.0</td>
      <td>7200</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>3</td>
      <td>98.0</td>
      <td>11478</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>3</td>
      <td>47.0</td>
      <td>16321</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>4</td>
      <td>60.0</td>
      <td>6324</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>3</td>
      <td>60.0</td>
      <td>21930</td>
      <td>1</td>
      <td>-1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>3</td>
      <td>0.0</td>
      <td>4928</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>3</td>
      <td>60.0</td>
      <td>10800</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>3</td>
      <td>93.0</td>
      <td>10261</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>17400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>8400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>0</td>
      <td>0</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>3</td>
      <td>60.0</td>
      <td>9000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>3</td>
      <td>96.0</td>
      <td>12444</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>6</td>
      <td>5</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>4</td>
      <td>90.0</td>
      <td>7407</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>3</td>
      <td>80.0</td>
      <td>11584</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>3</td>
      <td>79.0</td>
      <td>11526</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>4</td>
      <td>0.0</td>
      <td>4426</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>1</td>
      <td>85.0</td>
      <td>11003</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>3</td>
      <td>0.0</td>
      <td>8854</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>3</td>
      <td>63.0</td>
      <td>8500</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>3</td>
      <td>70.0</td>
      <td>8400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>26142</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>3</td>
      <td>80.0</td>
      <td>10000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>3</td>
      <td>70.0</td>
      <td>11767</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>4</td>
      <td>21.0</td>
      <td>1533</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>3</td>
      <td>60.0</td>
      <td>9000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>3</td>
      <td>78.0</td>
      <td>9262</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>6</td>
      <td>5</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>4</td>
      <td>35.0</td>
      <td>3675</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>3</td>
      <td>90.0</td>
      <td>17217</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>1</td>
      <td>62.0</td>
      <td>7500</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>3</td>
      <td>62.0</td>
      <td>7917</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>3</td>
      <td>85.0</td>
      <td>13175</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>3</td>
      <td>66.0</td>
      <td>9042</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>3</td>
      <td>68.0</td>
      <td>9717</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>9937</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 80 columns</p>
</div>




```python
x=pd.DataFrame(dfwtcatencode.isnull().sum(), columns=['Missing values'])
x
x[x["Missing values"] > 0]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Missing values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MasVnrArea</th>
      <td>8</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>81</td>
    </tr>
  </tbody>
</table>
</div>



* fill MasVnrArea missing values with min value which is zeros.


```python
df["MasVnrArea"]=dfwtcatencode["MasVnrArea"]=dfwtcatencode["MasVnrArea"].fillna(0)
dfwtcatencode
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>3</td>
      <td>65.0</td>
      <td>8450</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>9600</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>3</td>
      <td>68.0</td>
      <td>11250</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>3</td>
      <td>60.0</td>
      <td>9550</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>3</td>
      <td>84.0</td>
      <td>14260</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>3</td>
      <td>85.0</td>
      <td>14115</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>2</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>10084</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>3</td>
      <td>0.0</td>
      <td>10382</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>4</td>
      <td>51.0</td>
      <td>6120</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>8</td>
      <td>0</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>3</td>
      <td>50.0</td>
      <td>7420</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>3</td>
      <td>70.0</td>
      <td>11200</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>3</td>
      <td>85.0</td>
      <td>11924</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>6</td>
      <td>5</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>12968</td>
      <td>1</td>
      <td>-1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>3</td>
      <td>91.0</td>
      <td>10652</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>6</td>
      <td>5</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>10920</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>4</td>
      <td>51.0</td>
      <td>6120</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>11241</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>3</td>
      <td>72.0</td>
      <td>10791</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>2</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>3</td>
      <td>66.0</td>
      <td>13695</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>3</td>
      <td>70.0</td>
      <td>7560</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>0</td>
      <td>0</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>3</td>
      <td>101.0</td>
      <td>14215</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>6</td>
      <td>5</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>4</td>
      <td>57.0</td>
      <td>7449</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>9742</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>4</td>
      <td>44.0</td>
      <td>4224</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>8246</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>3</td>
      <td>110.0</td>
      <td>14230</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>3</td>
      <td>60.0</td>
      <td>7200</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>3</td>
      <td>98.0</td>
      <td>11478</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>3</td>
      <td>47.0</td>
      <td>16321</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>4</td>
      <td>60.0</td>
      <td>6324</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>3</td>
      <td>60.0</td>
      <td>21930</td>
      <td>1</td>
      <td>-1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>3</td>
      <td>0.0</td>
      <td>4928</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>3</td>
      <td>60.0</td>
      <td>10800</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>3</td>
      <td>93.0</td>
      <td>10261</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>17400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>3</td>
      <td>80.0</td>
      <td>8400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>0</td>
      <td>0</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>3</td>
      <td>60.0</td>
      <td>9000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>3</td>
      <td>96.0</td>
      <td>12444</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>6</td>
      <td>5</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>4</td>
      <td>90.0</td>
      <td>7407</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>3</td>
      <td>80.0</td>
      <td>11584</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>3</td>
      <td>79.0</td>
      <td>11526</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>4</td>
      <td>0.0</td>
      <td>4426</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>1</td>
      <td>85.0</td>
      <td>11003</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>3</td>
      <td>0.0</td>
      <td>8854</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>3</td>
      <td>63.0</td>
      <td>8500</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>3</td>
      <td>70.0</td>
      <td>8400</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>3</td>
      <td>0.0</td>
      <td>26142</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>3</td>
      <td>80.0</td>
      <td>10000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>3</td>
      <td>70.0</td>
      <td>11767</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>4</td>
      <td>21.0</td>
      <td>1533</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>3</td>
      <td>60.0</td>
      <td>9000</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>3</td>
      <td>78.0</td>
      <td>9262</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>6</td>
      <td>5</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>4</td>
      <td>35.0</td>
      <td>3675</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>8</td>
      <td>4</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>3</td>
      <td>90.0</td>
      <td>17217</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>8</td>
      <td>0</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>1</td>
      <td>62.0</td>
      <td>7500</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>8</td>
      <td>4</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>3</td>
      <td>62.0</td>
      <td>7917</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>8</td>
      <td>4</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>3</td>
      <td>85.0</td>
      <td>13175</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>3</td>
      <td>66.0</td>
      <td>9042</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>2</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>3</td>
      <td>68.0</td>
      <td>9717</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>8</td>
      <td>4</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>3</td>
      <td>75.0</td>
      <td>9937</td>
      <td>1</td>
      <td>-1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
      <td>...</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>8</td>
      <td>4</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 80 columns</p>
</div>




```python
garageCols=dfwtcatencode.filter(like='Garage')
garageCols[garageCols["GarageArea"] ==0 ]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GarageType</th>
      <th>GarageYrBlt</th>
      <th>GarageFinish</th>
      <th>GarageCars</th>
      <th>GarageArea</th>
      <th>GarageQual</th>
      <th>GarageCond</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>48</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>78</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>88</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>89</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>99</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>108</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>125</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>127</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>140</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>148</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>155</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>163</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>165</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>198</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>210</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>241</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>250</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>287</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>291</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>307</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>375</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>386</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>393</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>431</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>434</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>441</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>464</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>495</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>520</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>954</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>960</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>968</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>970</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>976</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1009</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1011</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1030</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1038</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1096</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1123</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1131</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1137</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1143</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1173</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1179</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1218</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1219</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1234</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1257</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1283</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1323</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1325</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1326</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1349</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1407</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>-1</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>-1</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
<p>81 rows × 7 columns</p>
</div>




```python
df=df.drop(df[df.GarageArea ==0].index)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>RL</td>
      <td>85.0</td>
      <td>14115</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>Shed</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>10084</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>RL</td>
      <td>0.0</td>
      <td>10382</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>RM</td>
      <td>51.0</td>
      <td>6120</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>RL</td>
      <td>50.0</td>
      <td>7420</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>RL</td>
      <td>70.0</td>
      <td>11200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>RL</td>
      <td>85.0</td>
      <td>11924</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>New</td>
      <td>Partial</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>RL</td>
      <td>0.0</td>
      <td>12968</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR2</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>RL</td>
      <td>91.0</td>
      <td>10652</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>New</td>
      <td>Partial</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>RL</td>
      <td>0.0</td>
      <td>10920</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>RM</td>
      <td>51.0</td>
      <td>6120</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>RL</td>
      <td>0.0</td>
      <td>11241</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>RL</td>
      <td>72.0</td>
      <td>10791</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shed</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>RL</td>
      <td>66.0</td>
      <td>13695</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>RL</td>
      <td>70.0</td>
      <td>7560</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>COD</td>
      <td>Abnorml</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>RL</td>
      <td>101.0</td>
      <td>14215</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>New</td>
      <td>Partial</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>RM</td>
      <td>57.0</td>
      <td>7449</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9742</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>RM</td>
      <td>44.0</td>
      <td>4224</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>RL</td>
      <td>0.0</td>
      <td>8246</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>RL</td>
      <td>110.0</td>
      <td>14230</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>RL</td>
      <td>60.0</td>
      <td>7200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>RL</td>
      <td>98.0</td>
      <td>11478</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>RL</td>
      <td>47.0</td>
      <td>16321</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>RM</td>
      <td>60.0</td>
      <td>6324</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1427</th>
      <td>50</td>
      <td>RL</td>
      <td>60.0</td>
      <td>10930</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>1428</th>
      <td>30</td>
      <td>RM</td>
      <td>60.0</td>
      <td>7200</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>WD</td>
      <td>Abnorml</td>
      <td>119000</td>
    </tr>
    <tr>
      <th>1429</th>
      <td>20</td>
      <td>RL</td>
      <td>0.0</td>
      <td>12546</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>182900</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>RL</td>
      <td>60.0</td>
      <td>21930</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR3</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>RL</td>
      <td>0.0</td>
      <td>4928</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>RL</td>
      <td>60.0</td>
      <td>10800</td>
      <td>Pave</td>
      <td>Grvl</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>RL</td>
      <td>93.0</td>
      <td>10261</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>17400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>RL</td>
      <td>80.0</td>
      <td>8400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>COD</td>
      <td>Abnorml</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>RL</td>
      <td>96.0</td>
      <td>12444</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>New</td>
      <td>Partial</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>RM</td>
      <td>90.0</td>
      <td>7407</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>11584</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>RL</td>
      <td>79.0</td>
      <td>11526</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Bnk</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>RM</td>
      <td>0.0</td>
      <td>4426</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>FV</td>
      <td>85.0</td>
      <td>11003</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>RL</td>
      <td>0.0</td>
      <td>8854</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>RL</td>
      <td>63.0</td>
      <td>8500</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>RL</td>
      <td>70.0</td>
      <td>8400</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>RL</td>
      <td>0.0</td>
      <td>26142</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>RL</td>
      <td>80.0</td>
      <td>10000</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>RL</td>
      <td>70.0</td>
      <td>11767</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdWo</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>RL</td>
      <td>78.0</td>
      <td>9262</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>New</td>
      <td>Partial</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>RM</td>
      <td>35.0</td>
      <td>3675</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>FV</td>
      <td>62.0</td>
      <td>7500</td>
      <td>Pave</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>WD</td>
      <td>Normal</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>RL</td>
      <td>62.0</td>
      <td>7917</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>WD</td>
      <td>Normal</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>RL</td>
      <td>85.0</td>
      <td>13175</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>RL</td>
      <td>66.0</td>
      <td>9042</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>Shed</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>RL</td>
      <td>68.0</td>
      <td>9717</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9937</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>WD</td>
      <td>Normal</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1379 rows × 80 columns</p>
</div>




```python
df.SalePrice.skew()
```




    1.8828757597682129




```python
plt.figure()
df["SalePrice"].plot.hist()
plt.show()
```


![png](output_53_0.png)



```python
dfwtcatencode=dfwtcatencode.drop(dfwtcatencode[dfwtcatencode.GarageArea == 0].index)
```


```python
dfwtcatencode["GarageYrBlt"].isnull().sum()
```




    0




```python
dfnumcols=df.select_dtypes(include=[np.number])
dfnumcols
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>OverallQual</th>
      <th>OverallCond</th>
      <th>YearBuilt</th>
      <th>YearRemodAdd</th>
      <th>MasVnrArea</th>
      <th>BsmtFinSF1</th>
      <th>BsmtFinSF2</th>
      <th>...</th>
      <th>WoodDeckSF</th>
      <th>OpenPorchSF</th>
      <th>EnclosedPorch</th>
      <th>3SsnPorch</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>65.0</td>
      <td>8450</td>
      <td>7</td>
      <td>5</td>
      <td>2003</td>
      <td>2003</td>
      <td>196.0</td>
      <td>706</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>61</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>208500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>80.0</td>
      <td>9600</td>
      <td>6</td>
      <td>8</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>978</td>
      <td>0</td>
      <td>...</td>
      <td>298</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>181500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>60</td>
      <td>68.0</td>
      <td>11250</td>
      <td>7</td>
      <td>5</td>
      <td>2001</td>
      <td>2002</td>
      <td>162.0</td>
      <td>486</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>223500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>60.0</td>
      <td>9550</td>
      <td>7</td>
      <td>5</td>
      <td>1915</td>
      <td>1970</td>
      <td>0.0</td>
      <td>216</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>35</td>
      <td>272</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2006</td>
      <td>140000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>84.0</td>
      <td>14260</td>
      <td>8</td>
      <td>5</td>
      <td>2000</td>
      <td>2000</td>
      <td>350.0</td>
      <td>655</td>
      <td>0</td>
      <td>...</td>
      <td>192</td>
      <td>84</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2008</td>
      <td>250000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>85.0</td>
      <td>14115</td>
      <td>5</td>
      <td>5</td>
      <td>1993</td>
      <td>1995</td>
      <td>0.0</td>
      <td>732</td>
      <td>0</td>
      <td>...</td>
      <td>40</td>
      <td>30</td>
      <td>0</td>
      <td>320</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>10</td>
      <td>2009</td>
      <td>143000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>75.0</td>
      <td>10084</td>
      <td>8</td>
      <td>5</td>
      <td>2004</td>
      <td>2005</td>
      <td>186.0</td>
      <td>1369</td>
      <td>0</td>
      <td>...</td>
      <td>255</td>
      <td>57</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>307000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>60</td>
      <td>0.0</td>
      <td>10382</td>
      <td>7</td>
      <td>6</td>
      <td>1973</td>
      <td>1973</td>
      <td>240.0</td>
      <td>859</td>
      <td>32</td>
      <td>...</td>
      <td>235</td>
      <td>204</td>
      <td>228</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>350</td>
      <td>11</td>
      <td>2009</td>
      <td>200000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>50</td>
      <td>51.0</td>
      <td>6120</td>
      <td>7</td>
      <td>5</td>
      <td>1931</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>90</td>
      <td>0</td>
      <td>205</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2008</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>9</th>
      <td>190</td>
      <td>50.0</td>
      <td>7420</td>
      <td>5</td>
      <td>6</td>
      <td>1939</td>
      <td>1950</td>
      <td>0.0</td>
      <td>851</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2008</td>
      <td>118000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>20</td>
      <td>70.0</td>
      <td>11200</td>
      <td>5</td>
      <td>5</td>
      <td>1965</td>
      <td>1965</td>
      <td>0.0</td>
      <td>906</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2008</td>
      <td>129500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>60</td>
      <td>85.0</td>
      <td>11924</td>
      <td>9</td>
      <td>5</td>
      <td>2005</td>
      <td>2006</td>
      <td>286.0</td>
      <td>998</td>
      <td>0</td>
      <td>...</td>
      <td>147</td>
      <td>21</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>20</td>
      <td>0.0</td>
      <td>12968</td>
      <td>5</td>
      <td>6</td>
      <td>1962</td>
      <td>1962</td>
      <td>0.0</td>
      <td>737</td>
      <td>0</td>
      <td>...</td>
      <td>140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>176</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>144000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>20</td>
      <td>91.0</td>
      <td>10652</td>
      <td>7</td>
      <td>5</td>
      <td>2006</td>
      <td>2007</td>
      <td>306.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>160</td>
      <td>33</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>279500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>20</td>
      <td>0.0</td>
      <td>10920</td>
      <td>6</td>
      <td>5</td>
      <td>1960</td>
      <td>1960</td>
      <td>212.0</td>
      <td>733</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>213</td>
      <td>176</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>157000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>45</td>
      <td>51.0</td>
      <td>6120</td>
      <td>7</td>
      <td>8</td>
      <td>1929</td>
      <td>2001</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>48</td>
      <td>112</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2007</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>0.0</td>
      <td>11241</td>
      <td>6</td>
      <td>7</td>
      <td>1970</td>
      <td>1970</td>
      <td>180.0</td>
      <td>578</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>3</td>
      <td>2010</td>
      <td>149000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>90</td>
      <td>72.0</td>
      <td>10791</td>
      <td>4</td>
      <td>5</td>
      <td>1967</td>
      <td>1967</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>500</td>
      <td>10</td>
      <td>2006</td>
      <td>90000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>20</td>
      <td>66.0</td>
      <td>13695</td>
      <td>5</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>0.0</td>
      <td>646</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>102</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>159000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>70.0</td>
      <td>7560</td>
      <td>5</td>
      <td>6</td>
      <td>1958</td>
      <td>1965</td>
      <td>0.0</td>
      <td>504</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>139000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>60</td>
      <td>101.0</td>
      <td>14215</td>
      <td>8</td>
      <td>5</td>
      <td>2005</td>
      <td>2006</td>
      <td>380.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>240</td>
      <td>154</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>325300</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45</td>
      <td>57.0</td>
      <td>7449</td>
      <td>7</td>
      <td>7</td>
      <td>1930</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>205</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>139400</td>
    </tr>
    <tr>
      <th>22</th>
      <td>20</td>
      <td>75.0</td>
      <td>9742</td>
      <td>8</td>
      <td>5</td>
      <td>2002</td>
      <td>2002</td>
      <td>281.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>171</td>
      <td>159</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>230000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>120</td>
      <td>44.0</td>
      <td>4224</td>
      <td>5</td>
      <td>7</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>840</td>
      <td>0</td>
      <td>...</td>
      <td>100</td>
      <td>110</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2007</td>
      <td>129900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20</td>
      <td>0.0</td>
      <td>8246</td>
      <td>5</td>
      <td>8</td>
      <td>1968</td>
      <td>2001</td>
      <td>0.0</td>
      <td>188</td>
      <td>668</td>
      <td>...</td>
      <td>406</td>
      <td>90</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>154000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>20</td>
      <td>110.0</td>
      <td>14230</td>
      <td>8</td>
      <td>5</td>
      <td>2007</td>
      <td>2007</td>
      <td>640.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>56</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2009</td>
      <td>256300</td>
    </tr>
    <tr>
      <th>26</th>
      <td>20</td>
      <td>60.0</td>
      <td>7200</td>
      <td>5</td>
      <td>7</td>
      <td>1951</td>
      <td>2000</td>
      <td>0.0</td>
      <td>234</td>
      <td>486</td>
      <td>...</td>
      <td>222</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>134800</td>
    </tr>
    <tr>
      <th>27</th>
      <td>20</td>
      <td>98.0</td>
      <td>11478</td>
      <td>8</td>
      <td>5</td>
      <td>2007</td>
      <td>2008</td>
      <td>200.0</td>
      <td>1218</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>306000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>20</td>
      <td>47.0</td>
      <td>16321</td>
      <td>5</td>
      <td>6</td>
      <td>1957</td>
      <td>1997</td>
      <td>0.0</td>
      <td>1277</td>
      <td>0</td>
      <td>...</td>
      <td>288</td>
      <td>258</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2006</td>
      <td>207500</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>60.0</td>
      <td>6324</td>
      <td>4</td>
      <td>6</td>
      <td>1927</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>49</td>
      <td>0</td>
      <td>87</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>68500</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>60</td>
      <td>60.0</td>
      <td>21930</td>
      <td>5</td>
      <td>5</td>
      <td>2005</td>
      <td>2005</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>100</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>192140</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>120</td>
      <td>0.0</td>
      <td>4928</td>
      <td>6</td>
      <td>6</td>
      <td>1976</td>
      <td>1976</td>
      <td>0.0</td>
      <td>958</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>143750</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>30</td>
      <td>60.0</td>
      <td>10800</td>
      <td>4</td>
      <td>6</td>
      <td>1927</td>
      <td>2007</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>64500</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>60</td>
      <td>93.0</td>
      <td>10261</td>
      <td>6</td>
      <td>5</td>
      <td>2000</td>
      <td>2000</td>
      <td>318.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>186500</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>20</td>
      <td>80.0</td>
      <td>17400</td>
      <td>5</td>
      <td>5</td>
      <td>1977</td>
      <td>1977</td>
      <td>0.0</td>
      <td>936</td>
      <td>0</td>
      <td>...</td>
      <td>295</td>
      <td>41</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>160000</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>20</td>
      <td>80.0</td>
      <td>8400</td>
      <td>6</td>
      <td>9</td>
      <td>1962</td>
      <td>2005</td>
      <td>237.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2008</td>
      <td>174000</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>20</td>
      <td>60.0</td>
      <td>9000</td>
      <td>4</td>
      <td>6</td>
      <td>1971</td>
      <td>1971</td>
      <td>0.0</td>
      <td>616</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>120500</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>20</td>
      <td>96.0</td>
      <td>12444</td>
      <td>8</td>
      <td>5</td>
      <td>2008</td>
      <td>2008</td>
      <td>426.0</td>
      <td>1336</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>66</td>
      <td>0</td>
      <td>304</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2008</td>
      <td>394617</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>20</td>
      <td>90.0</td>
      <td>7407</td>
      <td>6</td>
      <td>7</td>
      <td>1957</td>
      <td>1996</td>
      <td>0.0</td>
      <td>600</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>158</td>
      <td>158</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>149700</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>60</td>
      <td>80.0</td>
      <td>11584</td>
      <td>7</td>
      <td>6</td>
      <td>1979</td>
      <td>1979</td>
      <td>96.0</td>
      <td>315</td>
      <td>110</td>
      <td>...</td>
      <td>0</td>
      <td>88</td>
      <td>216</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>197000</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>70</td>
      <td>79.0</td>
      <td>11526</td>
      <td>6</td>
      <td>7</td>
      <td>1922</td>
      <td>1994</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>431</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2008</td>
      <td>191000</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>120</td>
      <td>0.0</td>
      <td>4426</td>
      <td>6</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>147.0</td>
      <td>697</td>
      <td>0</td>
      <td>...</td>
      <td>149</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2008</td>
      <td>149300</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>60</td>
      <td>85.0</td>
      <td>11003</td>
      <td>10</td>
      <td>5</td>
      <td>2008</td>
      <td>2008</td>
      <td>160.0</td>
      <td>765</td>
      <td>0</td>
      <td>...</td>
      <td>168</td>
      <td>52</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2009</td>
      <td>310000</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>30</td>
      <td>0.0</td>
      <td>8854</td>
      <td>6</td>
      <td>6</td>
      <td>1916</td>
      <td>1950</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>98</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>121000</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>20</td>
      <td>63.0</td>
      <td>8500</td>
      <td>7</td>
      <td>5</td>
      <td>2004</td>
      <td>2004</td>
      <td>106.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>192</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2007</td>
      <td>179600</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>85</td>
      <td>70.0</td>
      <td>8400</td>
      <td>6</td>
      <td>5</td>
      <td>1966</td>
      <td>1966</td>
      <td>0.0</td>
      <td>187</td>
      <td>627</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>252</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>129000</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>20</td>
      <td>0.0</td>
      <td>26142</td>
      <td>5</td>
      <td>7</td>
      <td>1962</td>
      <td>1962</td>
      <td>189.0</td>
      <td>593</td>
      <td>0</td>
      <td>...</td>
      <td>261</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>157900</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>60</td>
      <td>80.0</td>
      <td>10000</td>
      <td>8</td>
      <td>5</td>
      <td>1995</td>
      <td>1996</td>
      <td>438.0</td>
      <td>1079</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>65</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>2007</td>
      <td>240000</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>50</td>
      <td>70.0</td>
      <td>11767</td>
      <td>4</td>
      <td>7</td>
      <td>1910</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>168</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2007</td>
      <td>112000</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>180</td>
      <td>21.0</td>
      <td>1533</td>
      <td>5</td>
      <td>7</td>
      <td>1970</td>
      <td>1970</td>
      <td>0.0</td>
      <td>553</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2006</td>
      <td>92000</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>90</td>
      <td>60.0</td>
      <td>9000</td>
      <td>5</td>
      <td>5</td>
      <td>1974</td>
      <td>1974</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>32</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>2009</td>
      <td>136000</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>20</td>
      <td>78.0</td>
      <td>9262</td>
      <td>8</td>
      <td>5</td>
      <td>2008</td>
      <td>2009</td>
      <td>194.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2009</td>
      <td>287090</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>180</td>
      <td>35.0</td>
      <td>3675</td>
      <td>5</td>
      <td>5</td>
      <td>2005</td>
      <td>2005</td>
      <td>80.0</td>
      <td>547</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>28</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2006</td>
      <td>145000</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>20</td>
      <td>90.0</td>
      <td>17217</td>
      <td>5</td>
      <td>5</td>
      <td>2006</td>
      <td>2006</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>36</td>
      <td>56</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>2006</td>
      <td>84500</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>20</td>
      <td>62.0</td>
      <td>7500</td>
      <td>7</td>
      <td>5</td>
      <td>2004</td>
      <td>2005</td>
      <td>0.0</td>
      <td>410</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>113</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>2009</td>
      <td>185000</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>60</td>
      <td>62.0</td>
      <td>7917</td>
      <td>6</td>
      <td>5</td>
      <td>1999</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>40</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>2007</td>
      <td>175000</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>20</td>
      <td>85.0</td>
      <td>13175</td>
      <td>6</td>
      <td>6</td>
      <td>1978</td>
      <td>1988</td>
      <td>119.0</td>
      <td>790</td>
      <td>163</td>
      <td>...</td>
      <td>349</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2010</td>
      <td>210000</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>70</td>
      <td>66.0</td>
      <td>9042</td>
      <td>7</td>
      <td>9</td>
      <td>1941</td>
      <td>2006</td>
      <td>0.0</td>
      <td>275</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>60</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2500</td>
      <td>5</td>
      <td>2010</td>
      <td>266500</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>20</td>
      <td>68.0</td>
      <td>9717</td>
      <td>5</td>
      <td>6</td>
      <td>1950</td>
      <td>1996</td>
      <td>0.0</td>
      <td>49</td>
      <td>1029</td>
      <td>...</td>
      <td>366</td>
      <td>0</td>
      <td>112</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>142125</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20</td>
      <td>75.0</td>
      <td>9937</td>
      <td>5</td>
      <td>6</td>
      <td>1965</td>
      <td>1965</td>
      <td>0.0</td>
      <td>830</td>
      <td>290</td>
      <td>...</td>
      <td>736</td>
      <td>68</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2008</td>
      <td>147500</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 37 columns</p>
</div>




```python
dfspcorr=dfnumcols.corr()["SalePrice"]
```


```python
dfspcorr.sort_values()[:5]
```




    KitchenAbvGr    -0.135907
    EnclosedPorch   -0.128578
    MSSubClass      -0.084284
    OverallCond     -0.077856
    YrSold          -0.028923
    Name: SalePrice, dtype: float64




```python
dfspcorr.sort_values()[-10:]
```




    YearBuilt       0.522897
    TotRmsAbvGrd    0.533723
    FullBath        0.560664
    1stFlrSF        0.605852
    TotalBsmtSF     0.613581
    GarageArea      0.623431
    GarageCars      0.640409
    GrLivArea       0.708624
    OverallQual     0.790982
    SalePrice       1.000000
    Name: SalePrice, dtype: float64



Feature selection - forward chaining
select features with correlation and add others one by one


```python
df.plot.scatter(x="OverallQual",y="SalePrice")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5a9eec3c8>




![png](output_61_1.png)



```python
dfgbyovpsp=df.groupby('OverallQual').SalePrice
dfgbyovpsp.mean().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5a831e3c8>




![png](output_62_1.png)



```python
dfgbyovpsp.median().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5c3ec39e8>




![png](output_63_1.png)



```python
dfgbyovpsp.min().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5c1e29e10>




![png](output_64_1.png)



```python
dfgbyovpsp.max().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5a96b65f8>




![png](output_65_1.png)



```python
df.plot.scatter(x="GrLivArea", y="SalePrice")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5b12ede10>




![png](output_66_1.png)



```python
df.plot.scatter(x="GarageArea", y="SalePrice")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5caf1fc88>




![png](output_67_1.png)



```python
df.plot.scatter(x="GarageArea", y="TotalBsmtSF")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5aafe4588>




![png](output_68_1.png)



```python
df.plot.scatter(x="1stFlrSF", y="SalePrice")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5b008c390>




![png](output_69_1.png)



```python
df.plot.scatter(x="FullBath", y="SalePrice")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5c1e3df98>




![png](output_70_1.png)



```python
df.groupby("FullBath").SalePrice.mean().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5b008df28>




![png](output_71_1.png)



```python
df.groupby("FullBath").SalePrice.sum().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5b0f2b400>




![png](output_72_1.png)



```python
df.groupby("FullBath").SalePrice.median().plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7fc5aafc1080>




![png](output_73_1.png)



```python
pd.get_dummies(df.Street)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Grvl</th>
      <th>Pave</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 2 columns</p>
</div>




```python
dfwtcatencode.isnull().sum()
```




    MSSubClass       0
    MSZoning         0
    LotFrontage      0
    LotArea          0
    Street           0
    Alley            0
    LotShape         0
    LandContour      0
    Utilities        0
    LotConfig        0
    LandSlope        0
    Neighborhood     0
    Condition1       0
    Condition2       0
    BldgType         0
    HouseStyle       0
    OverallQual      0
    OverallCond      0
    YearBuilt        0
    YearRemodAdd     0
    RoofStyle        0
    RoofMatl         0
    Exterior1st      0
    Exterior2nd      0
    MasVnrType       0
    MasVnrArea       0
    ExterQual        0
    ExterCond        0
    Foundation       0
    BsmtQual         0
                    ..
    BedroomAbvGr     0
    KitchenAbvGr     0
    KitchenQual      0
    TotRmsAbvGrd     0
    Functional       0
    Fireplaces       0
    FireplaceQu      0
    GarageType       0
    GarageYrBlt      0
    GarageFinish     0
    GarageCars       0
    GarageArea       0
    GarageQual       0
    GarageCond       0
    PavedDrive       0
    WoodDeckSF       0
    OpenPorchSF      0
    EnclosedPorch    0
    3SsnPorch        0
    ScreenPorch      0
    PoolArea         0
    PoolQC           0
    Fence            0
    MiscFeature      0
    MiscVal          0
    MoSold           0
    YrSold           0
    SaleType         0
    SaleCondition    0
    SalePrice        0
    dtype: int64




```python
# dependent variable
y = np.log(dfwtcatencode.SalePrice)
X = dfwtcatencode.drop(["SalePrice"], axis=1)
```


```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
```


```python
from sklearn.linear_model import LinearRegression

model=LinearRegression().fit(X_train,y_train)
model.score(X_test,y_test)
```




    0.71476260038978945




```python
predictions=model.predict(X_test)
predictions
```




    array([ 12.44957875,  11.73110665,  11.4314049 ,  12.22642558,
            12.18313685,  11.40216856,  12.30122755,  12.2166647 ,
            11.98887905,  12.18568801,  11.58317881,  12.59381249,
            11.67479061,  12.65918155,  12.05330083,  11.86410614,
            12.33706687,  11.7993828 ,  12.24636831,  12.54591471,
            11.68988252,  11.95004048,  12.01285174,  12.40941295,
            12.90211327,  12.0781378 ,  11.60931317,  11.66077275,
            12.76740804,  12.03882237,  12.45618035,  11.94191454,
            11.85870971,  11.7651146 ,  12.1648075 ,  13.018707  ,
            11.61225969,  11.57335727,  12.50458066,  12.13749893,
            12.05561083,  11.79285021,  12.0266296 ,  12.79781697,
            11.96292886,  12.45639039,  11.55494809,  12.33147112,
            11.62066082,  12.63973716,  11.86001563,  11.18460645,
            11.65521788,  12.03432151,  12.22301145,  11.67353559,
            11.7507798 ,  12.16174577,  11.98969167,  12.6093756 ,
            11.52003177,  12.03166148,  11.82900684,  12.62184653,
            11.11534778,  12.78497792,  12.01184349,  11.62373182,
            12.05335344,  12.19359581,  11.81891508,  12.47434077,
            11.686057  ,  11.85396094,  11.56375789,  11.70043774,
            11.37222015,  12.00012349,  12.46963165,  11.78121905,
            12.71065486,  12.26920524,  12.41480502,  12.24708687,
            11.77688347,  12.4239395 ,  11.84902162,  11.72526674,
            11.8990372 ,  12.519955  ,  12.48152663,  12.57435369,
            12.07605311,  12.06846015,  11.95098419,  12.26235855,
            12.35100099,  12.2574972 ,  12.49458594,  12.40095563,
            11.74976178,  11.66624646,  12.01633451,  12.11896875,
            11.89940575,  12.02507712,  12.1656753 ,  11.80880575,
            12.02149196,  12.10701706,  11.9654179 ,  11.65005123,
            12.76321717,  12.52959665,  12.68479337,  11.54448432,
            11.91904999,  12.37627121,  11.83973257,  12.15198549,
            12.18068213,  11.65307908,  11.68021432,  12.10208018,
            11.84086243,  12.16288197,  11.82834006,  12.5265057 ,
            11.96229861,  11.74390244,  12.65652436,  12.00807983,
            11.81947261,  11.84244848,  12.63901856,  11.88754278,
            12.48912408,  11.80966859,  11.36845838,  11.99238789,
            11.85816345,  11.93509873,  12.13934255,  12.4519455 ,
            11.83828769,  11.87113119,  12.39266278,  12.63219376,
            11.76940739,  12.19150142,  11.9196981 ,  11.9048348 ,
            11.65162449,  12.38095067,  12.73878025,  11.48277547,
            12.48036395,  11.56191023,  11.72125034,  12.09392787,
            12.18992547,  12.27325967,  11.98203332,  12.29329783,
            11.92356692,  11.78023515,  12.01270966,  12.82426236,
            11.88508443,  11.54525219,  11.78123707,  11.69892363,
            11.77243011,  11.94051719,  12.02665694,  12.48369027,
            12.17016565,  11.93088307,  11.75778799,  12.32523483,
            11.81919344,  12.47568884,  12.68951332,  11.72772608,
            11.83284151,  11.98801745,  11.85265293,  12.46026364,
            12.28055783,  11.85509798,  12.67138322,  11.84332741,
            12.4113505 ,  11.65222135,  11.65884478,  11.95432782,
            11.93040019,  12.9786354 ,  12.88111936,  12.55985867,
            12.50998648,  12.57787628,  12.72056309,  12.58413534,
            12.12615604,  11.57321142,  11.92472106,  11.68528585,
            12.17738763,  11.94490868,  11.52526051,  11.61612315,
            11.63064285,  12.66083643,  12.79724824,  12.41576763,
            11.90040659,  12.16586678,  11.88673859,  12.48174025,
            11.76600482,  11.75818441,  12.68121764,  12.05425534,
            12.07379925,  13.85753762,  11.96022601,  11.86650589,
            12.2722717 ,  11.47487668,  12.02607697,  12.82049308,
            11.79774069,  12.17581482,  11.7806752 ,  11.2659965 ,
            12.13727204,  12.4446952 ,  11.67314987,  12.12397107,
            12.17247133,  11.82885446,  11.84075753,  12.40709561,
            12.13087093,  13.00257524,  11.76882724,  11.80039119,
            12.36727268,  12.01792189,  11.55664989,  12.06317851,
            12.21135863,  12.25211212,  11.65401846,  11.41915243,
            12.36766321,  11.91109546,  11.68846296,  11.62978589,
            12.0118789 ,  12.04317565,  12.37619332,  12.51745163,
            11.70039148,  12.27333988,  12.05691357,  12.06708141,
            11.97261458,  12.26340337,  11.63002651,  11.78144058,
            12.03809913,  12.16483043,  12.15006465,  12.19446815,
             9.69456385,  11.77161733,  11.68666944,  12.38392539,
            11.89261339,  12.72622193,  12.18792366,  11.34175231,
            12.19258748,  11.6752492 ,  12.0901128 ,  11.53128133,
            12.15706446,  12.15648019,  12.09137192,  11.73763107,
            11.66555869,  12.26070209,  12.23675133,  12.15222166,
            12.48256379,  12.26419372,  11.72504933,  11.79086058,
            12.42990345,  11.71068254,  12.18688863,  11.72051477,
            12.24098353,  11.87524399,  11.89235255,  12.41250563,
            11.46694164,  11.44935055,  11.58123999,  12.64471095,
            10.45765659,  12.10369483,  12.19095653,  11.51961718,
            11.77120426,  11.74858471,  13.2423616 ,  11.82432477,
            11.73800642,  12.61087061,  12.27635083,  12.33502491,
            12.20010385,  11.54520251,  11.78414654,  12.19910736,
            11.88344278,  11.85910221,  11.98125547,  12.05604904,
            11.43092166,  12.02455911,  11.62997133,  11.92836009,
            12.07715064,  11.88650148,  11.87463044,  12.13825049,
            12.23722633,  11.59210951,  12.01021623,  12.27308549,
            12.24133924,  11.91525917,  12.54283104,  11.774026  ,
            12.67727421,  12.2328089 ,  11.83655224,  12.1347161 ,
            11.92781734,  11.72099354,  11.87280302,  11.66968968,
            11.60516909,  11.36703989,  11.33352469,  12.17869731,
            11.68289377,  11.6930139 ,  12.05029217,  11.54729269,
            12.47121326,  12.07164942,  12.6437853 ,  12.89518281,
            11.70518645,  11.75304191,  11.79305489,  11.83164717,
            11.3536219 ,  12.43007545,  12.27065117,  12.24786916,
            11.71513224,  12.06528691,  11.79490313,  11.66827593,
            12.30329879,  12.21258061,  11.58453252,  12.47974169,
            11.4330015 ,  12.16031609,  12.17762683,  11.81922539,
            12.10606339,  11.93644105,  12.49582459,  12.08653417,
            11.70752516,  12.59695342,  12.95842391,  12.90023318,
            11.78968746,  12.04697479,  11.36996411,  12.29509527,
            11.81073825,  12.62014425,  12.0430397 ,  11.88005506,
            11.86308247,  11.41423208,  12.06007129,  12.14753081,
            12.07455752,  11.24349622,  11.47740326,  12.15060001,
            11.90205044,  11.79527828,  11.5673319 ,  11.24118761,
            12.04415567,  11.79145049,  12.40592648,  11.89811975,
            12.09428902,  11.93074822,  12.07813616,  11.61142955,
            11.89297181,  11.07555326,  12.65481013,  12.91696564,
            12.17430068,  11.64821052,  11.64779388,  11.67273643,
            11.88987895,  12.02702933,  13.04560417,  11.45925383,
            11.93971284,  12.12288142,  12.06900464,  12.45211704,
            11.93715862,  11.7839728 ,  12.65881564,  12.95090886,
            12.86925248,  11.62625864,  12.78194377,  11.84597456,
            11.81132791,  12.71681049,  12.16579152,  12.19391686,
            11.68309883,  12.57407246,  11.58503633,  11.9446722 ])




```python
from sklearn.metrics import mean_squared_error

mean_squared_error(y_test,predictions)
```




    0.044391614506607169




```python
plt.scatter(predictions, y_test)
```




    <matplotlib.collections.PathCollection at 0x7fc5aae50588>




![png](output_81_1.png)



```python
dfspcorr.sort_values(ascending=False)
```




    SalePrice        1.000000
    OverallQual      0.790982
    GrLivArea        0.708624
    GarageCars       0.640409
    GarageArea       0.623431
    TotalBsmtSF      0.613581
    1stFlrSF         0.605852
    FullBath         0.560664
    TotRmsAbvGrd     0.533723
    YearBuilt        0.522897
    YearRemodAdd     0.507101
    GarageYrBlt      0.486362
    MasVnrArea       0.472614
    Fireplaces       0.466929
    BsmtFinSF1       0.386420
    Foundation       0.382479
    FireplaceQu      0.378377
    WoodDeckSF       0.324413
    2ndFlrSF         0.319334
    OpenPorchSF      0.315856
    HalfBath         0.284108
    GarageCond       0.275781
    LotArea          0.263843
    GarageQual       0.261347
    CentralAir       0.251328
    Electrical       0.233919
    PavedDrive       0.231357
    BsmtFullBath     0.227122
    RoofStyle        0.222405
    BsmtUnfSF        0.214479
                       ...   
    LandContour      0.015453
    Condition2       0.007513
    MasVnrType      -0.000488
    BsmtFinSF2      -0.011378
    BsmtFinType1    -0.013233
    Utilities       -0.014314
    BsmtHalfBath    -0.016844
    MiscVal         -0.021190
    LowQualFinSF    -0.025606
    YrSold          -0.028923
    SaleType        -0.054911
    LotConfig       -0.067396
    MiscFeature     -0.069317
    OverallCond     -0.077856
    MSSubClass      -0.084284
    BldgType        -0.085591
    Alley           -0.092607
    Heating         -0.098812
    EnclosedPorch   -0.128578
    KitchenAbvGr    -0.135907
    MSZoning        -0.166872
    Fence           -0.181911
    BsmtExposure    -0.193079
    GarageType      -0.223819
    LotShape        -0.255580
    GarageFinish    -0.292483
    HeatingQC       -0.400178
    BsmtQual        -0.438881
    KitchenQual     -0.589189
    ExterQual       -0.636884
    Name: SalePrice, dtype: float64




```python
df.groupby("FullBath").SalePrice.sum().plot.bar()
```


```python
dfwtcatencode.corr().SalePrice.sort_values()`
```




    ExterQual       -0.636884
    KitchenQual     -0.589189
    BsmtQual        -0.438881
    HeatingQC       -0.400178
    GarageFinish    -0.292483
    LotShape        -0.255580
    GarageType      -0.223819
    BsmtExposure    -0.193079
    Fence           -0.181911
    MSZoning        -0.166872
    KitchenAbvGr    -0.135907
    EnclosedPorch   -0.128578
    Heating         -0.098812
    Alley           -0.092607
    BldgType        -0.085591
    MSSubClass      -0.084284
    OverallCond     -0.077856
    MiscFeature     -0.069317
    LotConfig       -0.067396
    SaleType        -0.054911
    YrSold          -0.028923
    LowQualFinSF    -0.025606
    MiscVal         -0.021190
    BsmtHalfBath    -0.016844
    Utilities       -0.014314
    BsmtFinType1    -0.013233
    BsmtFinSF2      -0.011378
    MasVnrType      -0.000488
    Condition2       0.007513
    LandContour      0.015453
                       ...   
    BsmtUnfSF        0.214479
    RoofStyle        0.222405
    BsmtFullBath     0.227122
    PavedDrive       0.231357
    Electrical       0.233919
    CentralAir       0.251328
    GarageQual       0.261347
    LotArea          0.263843
    GarageCond       0.275781
    HalfBath         0.284108
    OpenPorchSF      0.315856
    2ndFlrSF         0.319334
    WoodDeckSF       0.324413
    FireplaceQu      0.378377
    Foundation       0.382479
    BsmtFinSF1       0.386420
    Fireplaces       0.466929
    MasVnrArea       0.472614
    GarageYrBlt      0.486362
    YearRemodAdd     0.507101
    YearBuilt        0.522897
    TotRmsAbvGrd     0.533723
    FullBath         0.560664
    1stFlrSF         0.605852
    TotalBsmtSF      0.613581
    GarageArea       0.623431
    GarageCars       0.640409
    GrLivArea        0.708624
    OverallQual      0.790982
    SalePrice        1.000000
    Name: SalePrice, dtype: float64




```python
dfwtcatencode.corr().SalePrice.sort_values()[-5:]
```




    GarageArea     0.623431
    GarageCars     0.640409
    GrLivArea      0.708624
    OverallQual    0.790982
    SalePrice      1.000000
    Name: SalePrice, dtype: float64




```python
dfwtcatencode.corr().SalePrice.sort_values()[:5]
```




    ExterQual      -0.636884
    KitchenQual    -0.589189
    BsmtQual       -0.438881
    HeatingQC      -0.400178
    GarageFinish   -0.292483
    Name: SalePrice, dtype: float64




```python
dfwtcatencode.filter(like="Bsmt")
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BsmtQual</th>
      <th>BsmtCond</th>
      <th>BsmtExposure</th>
      <th>BsmtFinType1</th>
      <th>BsmtFinSF1</th>
      <th>BsmtFinType2</th>
      <th>BsmtFinSF2</th>
      <th>BsmtUnfSF</th>
      <th>TotalBsmtSF</th>
      <th>BsmtFullBath</th>
      <th>BsmtHalfBath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>706</td>
      <td>5</td>
      <td>0</td>
      <td>150</td>
      <td>856</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>978</td>
      <td>5</td>
      <td>0</td>
      <td>284</td>
      <td>1262</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>486</td>
      <td>5</td>
      <td>0</td>
      <td>434</td>
      <td>920</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>216</td>
      <td>5</td>
      <td>0</td>
      <td>540</td>
      <td>756</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>655</td>
      <td>5</td>
      <td>0</td>
      <td>490</td>
      <td>1145</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>732</td>
      <td>5</td>
      <td>0</td>
      <td>64</td>
      <td>796</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>1369</td>
      <td>5</td>
      <td>0</td>
      <td>317</td>
      <td>1686</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>859</td>
      <td>1</td>
      <td>32</td>
      <td>216</td>
      <td>1107</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>952</td>
      <td>952</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>851</td>
      <td>5</td>
      <td>0</td>
      <td>140</td>
      <td>991</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>906</td>
      <td>5</td>
      <td>0</td>
      <td>134</td>
      <td>1040</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>998</td>
      <td>5</td>
      <td>0</td>
      <td>177</td>
      <td>1175</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>737</td>
      <td>5</td>
      <td>0</td>
      <td>175</td>
      <td>912</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1494</td>
      <td>1494</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>733</td>
      <td>5</td>
      <td>0</td>
      <td>520</td>
      <td>1253</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>832</td>
      <td>832</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>578</td>
      <td>5</td>
      <td>0</td>
      <td>426</td>
      <td>1004</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>-1</td>
      <td>0</td>
      <td>-1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>646</td>
      <td>5</td>
      <td>0</td>
      <td>468</td>
      <td>1114</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>504</td>
      <td>5</td>
      <td>0</td>
      <td>525</td>
      <td>1029</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1158</td>
      <td>1158</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>637</td>
      <td>637</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1777</td>
      <td>1777</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>840</td>
      <td>5</td>
      <td>0</td>
      <td>200</td>
      <td>1040</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>188</td>
      <td>0</td>
      <td>668</td>
      <td>204</td>
      <td>1060</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1566</td>
      <td>1566</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>234</td>
      <td>4</td>
      <td>486</td>
      <td>180</td>
      <td>900</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1218</td>
      <td>5</td>
      <td>0</td>
      <td>486</td>
      <td>1704</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1277</td>
      <td>5</td>
      <td>0</td>
      <td>207</td>
      <td>1484</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>520</td>
      <td>520</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>732</td>
      <td>732</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1431</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>958</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>958</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1432</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>656</td>
      <td>656</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>936</td>
      <td>936</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1434</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>936</td>
      <td>5</td>
      <td>0</td>
      <td>190</td>
      <td>1126</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1319</td>
      <td>1319</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1436</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>616</td>
      <td>5</td>
      <td>0</td>
      <td>248</td>
      <td>864</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1437</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>1336</td>
      <td>5</td>
      <td>0</td>
      <td>596</td>
      <td>1932</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1438</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>600</td>
      <td>5</td>
      <td>0</td>
      <td>312</td>
      <td>912</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1439</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>315</td>
      <td>4</td>
      <td>110</td>
      <td>114</td>
      <td>539</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1440</th>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>588</td>
      <td>588</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>697</td>
      <td>5</td>
      <td>0</td>
      <td>151</td>
      <td>848</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1442</th>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>765</td>
      <td>5</td>
      <td>0</td>
      <td>252</td>
      <td>1017</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>952</td>
      <td>952</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1444</th>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1422</td>
      <td>1422</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1445</th>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>187</td>
      <td>4</td>
      <td>627</td>
      <td>0</td>
      <td>814</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1446</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>593</td>
      <td>5</td>
      <td>0</td>
      <td>595</td>
      <td>1188</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1447</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1079</td>
      <td>5</td>
      <td>0</td>
      <td>141</td>
      <td>1220</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1448</th>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>560</td>
      <td>560</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1449</th>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>553</td>
      <td>5</td>
      <td>0</td>
      <td>77</td>
      <td>630</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1450</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>896</td>
      <td>896</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1451</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1573</td>
      <td>1573</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1452</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>547</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>547</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1453</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>1140</td>
      <td>1140</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1454</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>410</td>
      <td>5</td>
      <td>0</td>
      <td>811</td>
      <td>1221</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1455</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>953</td>
      <td>953</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>790</td>
      <td>4</td>
      <td>163</td>
      <td>589</td>
      <td>1542</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>275</td>
      <td>5</td>
      <td>0</td>
      <td>877</td>
      <td>1152</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>49</td>
      <td>4</td>
      <td>1029</td>
      <td>0</td>
      <td>1078</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>830</td>
      <td>3</td>
      <td>290</td>
      <td>136</td>
      <td>1256</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 11 columns</p>
</div>



## Feature Engineering


```python

```


```python
dfcatencode["MasVnrArea"]
```




    0       196.0
    1         0.0
    2       162.0
    3         0.0
    4       350.0
    5         0.0
    6       186.0
    7       240.0
    8         0.0
    9         0.0
    10        0.0
    11      286.0
    12        0.0
    13      306.0
    14      212.0
    15        0.0
    16      180.0
    17        0.0
    18        0.0
    19        0.0
    20      380.0
    21        0.0
    22      281.0
    23        0.0
    24        0.0
    25      640.0
    26        0.0
    27      200.0
    28        0.0
    29        0.0
            ...  
    1430      0.0
    1431      0.0
    1432      0.0
    1433    318.0
    1434      0.0
    1435    237.0
    1436      0.0
    1437    426.0
    1438      0.0
    1439     96.0
    1440      0.0
    1441    147.0
    1442    160.0
    1443      0.0
    1444    106.0
    1445      0.0
    1446    189.0
    1447    438.0
    1448      0.0
    1449      0.0
    1450      0.0
    1451    194.0
    1452     80.0
    1453      0.0
    1454      0.0
    1455      0.0
    1456    119.0
    1457      0.0
    1458      0.0
    1459      0.0
    Name: MasVnrArea, dtype: float64




```python
dfwtcatencode[dfwtcatencode["PoolArea"] > 0].loc[:,["PoolQC","PoolArea"]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PoolQC</th>
      <th>PoolArea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>197</th>
      <td>0</td>
      <td>512</td>
    </tr>
    <tr>
      <th>810</th>
      <td>1</td>
      <td>648</td>
    </tr>
    <tr>
      <th>1170</th>
      <td>2</td>
      <td>576</td>
    </tr>
    <tr>
      <th>1182</th>
      <td>0</td>
      <td>555</td>
    </tr>
    <tr>
      <th>1298</th>
      <td>2</td>
      <td>480</td>
    </tr>
    <tr>
      <th>1386</th>
      <td>1</td>
      <td>519</td>
    </tr>
    <tr>
      <th>1423</th>
      <td>2</td>
      <td>738</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure()
pd.value_counts(df["Alley"]).plot.bar()
plt.show()
```


![png](output_92_0.png)



```python
> Categorical missing data dependent on physical existence shown by other variable.

*FireplaceQu*
* 
```


```python
dfwtcatencode[ (dfwtcatencode["FireplaceQu"] == -1) & (dfwtcatencode["Fireplaces"] > 0) ].loc[:,["FireplaceQu","Fireplaces"]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FireplaceQu</th>
      <th>Fireplaces</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
from itertools import product
for cat,cont in product(catcols,["SalePrice"]):
    plt.figure()
    df.groupby(cat)[cont].sum().plot.bar()
```

    /usr/local/lib/python3.5/dist-packages/matplotlib/pyplot.py:524: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
      max_open_warning, RuntimeWarning)



![png](output_95_1.png)



![png](output_95_2.png)



![png](output_95_3.png)



![png](output_95_4.png)



![png](output_95_5.png)



![png](output_95_6.png)



![png](output_95_7.png)



![png](output_95_8.png)



![png](output_95_9.png)



![png](output_95_10.png)



![png](output_95_11.png)



![png](output_95_12.png)



![png](output_95_13.png)



![png](output_95_14.png)



![png](output_95_15.png)



![png](output_95_16.png)



![png](output_95_17.png)



![png](output_95_18.png)



![png](output_95_19.png)



![png](output_95_20.png)



![png](output_95_21.png)



![png](output_95_22.png)



![png](output_95_23.png)



![png](output_95_24.png)



![png](output_95_25.png)



![png](output_95_26.png)



![png](output_95_27.png)



![png](output_95_28.png)



![png](output_95_29.png)



![png](output_95_30.png)



![png](output_95_31.png)



![png](output_95_32.png)



![png](output_95_33.png)



![png](output_95_34.png)



![png](output_95_35.png)



![png](output_95_36.png)



![png](output_95_37.png)



![png](output_95_38.png)



![png](output_95_39.png)



![png](output_95_40.png)



![png](output_95_41.png)



![png](output_95_42.png)



![png](output_95_43.png)



```python
dfcont.corr()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>OverallQual</th>
      <th>OverallCond</th>
      <th>YearBuilt</th>
      <th>YearRemodAdd</th>
      <th>MasVnrArea</th>
      <th>BsmtFinSF1</th>
      <th>BsmtFinSF2</th>
      <th>...</th>
      <th>WoodDeckSF</th>
      <th>OpenPorchSF</th>
      <th>EnclosedPorch</th>
      <th>3SsnPorch</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>1.000000</td>
      <td>-0.386347</td>
      <td>-0.139781</td>
      <td>0.032628</td>
      <td>-0.059316</td>
      <td>0.027850</td>
      <td>0.040581</td>
      <td>0.022936</td>
      <td>-0.069836</td>
      <td>-0.065649</td>
      <td>...</td>
      <td>-0.012579</td>
      <td>-0.006100</td>
      <td>-0.012037</td>
      <td>-0.043825</td>
      <td>-0.026030</td>
      <td>0.008283</td>
      <td>-0.007683</td>
      <td>-0.013585</td>
      <td>-0.021407</td>
      <td>-0.084284</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>-0.386347</td>
      <td>1.000000</td>
      <td>0.426095</td>
      <td>0.251646</td>
      <td>-0.059213</td>
      <td>0.123349</td>
      <td>0.088866</td>
      <td>0.193458</td>
      <td>0.233633</td>
      <td>0.049900</td>
      <td>...</td>
      <td>0.088521</td>
      <td>0.151972</td>
      <td>0.010700</td>
      <td>0.070029</td>
      <td>0.041383</td>
      <td>0.206167</td>
      <td>0.003368</td>
      <td>0.011200</td>
      <td>0.007450</td>
      <td>0.351799</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>-0.139781</td>
      <td>0.426095</td>
      <td>1.000000</td>
      <td>0.105806</td>
      <td>-0.005636</td>
      <td>0.014228</td>
      <td>0.013788</td>
      <td>0.104160</td>
      <td>0.214103</td>
      <td>0.111170</td>
      <td>...</td>
      <td>0.171698</td>
      <td>0.084774</td>
      <td>-0.018340</td>
      <td>0.020423</td>
      <td>0.043160</td>
      <td>0.077672</td>
      <td>0.038068</td>
      <td>0.001205</td>
      <td>-0.014261</td>
      <td>0.263843</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>0.032628</td>
      <td>0.251646</td>
      <td>0.105806</td>
      <td>1.000000</td>
      <td>-0.091932</td>
      <td>0.572323</td>
      <td>0.550684</td>
      <td>0.411876</td>
      <td>0.239666</td>
      <td>-0.059119</td>
      <td>...</td>
      <td>0.238923</td>
      <td>0.308819</td>
      <td>-0.113937</td>
      <td>0.030371</td>
      <td>0.064886</td>
      <td>0.065166</td>
      <td>-0.031406</td>
      <td>0.070815</td>
      <td>-0.027347</td>
      <td>0.790982</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>-0.059316</td>
      <td>-0.059213</td>
      <td>-0.005636</td>
      <td>-0.091932</td>
      <td>1.000000</td>
      <td>-0.375983</td>
      <td>0.073741</td>
      <td>-0.128101</td>
      <td>-0.046231</td>
      <td>0.040229</td>
      <td>...</td>
      <td>-0.003334</td>
      <td>-0.032589</td>
      <td>0.070356</td>
      <td>0.025504</td>
      <td>0.054811</td>
      <td>-0.001985</td>
      <td>0.068777</td>
      <td>-0.003511</td>
      <td>0.043950</td>
      <td>-0.077856</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>0.027850</td>
      <td>0.123349</td>
      <td>0.014228</td>
      <td>0.572323</td>
      <td>-0.375983</td>
      <td>1.000000</td>
      <td>0.592855</td>
      <td>0.315707</td>
      <td>0.249503</td>
      <td>-0.049107</td>
      <td>...</td>
      <td>0.224880</td>
      <td>0.188686</td>
      <td>-0.387268</td>
      <td>0.031355</td>
      <td>-0.050364</td>
      <td>0.004950</td>
      <td>-0.034383</td>
      <td>0.012398</td>
      <td>-0.013618</td>
      <td>0.522897</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>0.040581</td>
      <td>0.088866</td>
      <td>0.013788</td>
      <td>0.550684</td>
      <td>0.073741</td>
      <td>0.592855</td>
      <td>1.000000</td>
      <td>0.179618</td>
      <td>0.128451</td>
      <td>-0.067759</td>
      <td>...</td>
      <td>0.205726</td>
      <td>0.226298</td>
      <td>-0.193919</td>
      <td>0.045286</td>
      <td>-0.038740</td>
      <td>0.005829</td>
      <td>-0.010286</td>
      <td>0.021490</td>
      <td>0.035743</td>
      <td>0.507101</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>0.022936</td>
      <td>0.193458</td>
      <td>0.104160</td>
      <td>0.411876</td>
      <td>-0.128101</td>
      <td>0.315707</td>
      <td>0.179618</td>
      <td>1.000000</td>
      <td>0.264736</td>
      <td>-0.072319</td>
      <td>...</td>
      <td>0.159718</td>
      <td>0.125703</td>
      <td>-0.110204</td>
      <td>0.018796</td>
      <td>0.061466</td>
      <td>0.011723</td>
      <td>-0.029815</td>
      <td>-0.005965</td>
      <td>-0.008201</td>
      <td>0.477493</td>
    </tr>
    <tr>
      <th>BsmtFinSF1</th>
      <td>-0.069836</td>
      <td>0.233633</td>
      <td>0.214103</td>
      <td>0.239666</td>
      <td>-0.046231</td>
      <td>0.249503</td>
      <td>0.128451</td>
      <td>0.264736</td>
      <td>1.000000</td>
      <td>-0.050117</td>
      <td>...</td>
      <td>0.204306</td>
      <td>0.111761</td>
      <td>-0.102303</td>
      <td>0.026451</td>
      <td>0.062021</td>
      <td>0.140491</td>
      <td>0.003571</td>
      <td>-0.015727</td>
      <td>0.014359</td>
      <td>0.386420</td>
    </tr>
    <tr>
      <th>BsmtFinSF2</th>
      <td>-0.065649</td>
      <td>0.049900</td>
      <td>0.111170</td>
      <td>-0.059119</td>
      <td>0.040229</td>
      <td>-0.049107</td>
      <td>-0.067759</td>
      <td>-0.072319</td>
      <td>-0.050117</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.067898</td>
      <td>0.003093</td>
      <td>0.036543</td>
      <td>-0.029993</td>
      <td>0.088871</td>
      <td>0.041709</td>
      <td>0.004940</td>
      <td>-0.015211</td>
      <td>0.031706</td>
      <td>-0.011378</td>
    </tr>
    <tr>
      <th>BsmtUnfSF</th>
      <td>-0.140759</td>
      <td>0.132644</td>
      <td>-0.002618</td>
      <td>0.308159</td>
      <td>-0.136841</td>
      <td>0.149040</td>
      <td>0.181133</td>
      <td>0.114442</td>
      <td>-0.495251</td>
      <td>-0.209294</td>
      <td>...</td>
      <td>-0.005316</td>
      <td>0.129005</td>
      <td>-0.002538</td>
      <td>0.020764</td>
      <td>-0.012579</td>
      <td>-0.035092</td>
      <td>-0.023837</td>
      <td>0.034888</td>
      <td>-0.041258</td>
      <td>0.214479</td>
    </tr>
    <tr>
      <th>TotalBsmtSF</th>
      <td>-0.238518</td>
      <td>0.392075</td>
      <td>0.260833</td>
      <td>0.537808</td>
      <td>-0.171098</td>
      <td>0.391452</td>
      <td>0.291066</td>
      <td>0.363936</td>
      <td>0.522396</td>
      <td>0.104810</td>
      <td>...</td>
      <td>0.232019</td>
      <td>0.247264</td>
      <td>-0.095478</td>
      <td>0.037384</td>
      <td>0.084489</td>
      <td>0.126053</td>
      <td>-0.018479</td>
      <td>0.013196</td>
      <td>-0.014969</td>
      <td>0.613581</td>
    </tr>
    <tr>
      <th>1stFlrSF</th>
      <td>-0.251758</td>
      <td>0.457181</td>
      <td>0.299475</td>
      <td>0.476224</td>
      <td>-0.144203</td>
      <td>0.281986</td>
      <td>0.240379</td>
      <td>0.344501</td>
      <td>0.445863</td>
      <td>0.097117</td>
      <td>...</td>
      <td>0.235459</td>
      <td>0.211671</td>
      <td>-0.065292</td>
      <td>0.056104</td>
      <td>0.088758</td>
      <td>0.131525</td>
      <td>-0.021096</td>
      <td>0.031372</td>
      <td>-0.013604</td>
      <td>0.605852</td>
    </tr>
    <tr>
      <th>2ndFlrSF</th>
      <td>0.307886</td>
      <td>0.080177</td>
      <td>0.050986</td>
      <td>0.295493</td>
      <td>0.028942</td>
      <td>0.010308</td>
      <td>0.140024</td>
      <td>0.174561</td>
      <td>-0.137079</td>
      <td>-0.099260</td>
      <td>...</td>
      <td>0.092165</td>
      <td>0.208026</td>
      <td>0.061989</td>
      <td>-0.024358</td>
      <td>0.040606</td>
      <td>0.081487</td>
      <td>0.016197</td>
      <td>0.035164</td>
      <td>-0.028700</td>
      <td>0.319334</td>
    </tr>
    <tr>
      <th>LowQualFinSF</th>
      <td>0.046474</td>
      <td>0.038469</td>
      <td>0.004779</td>
      <td>-0.030429</td>
      <td>0.025494</td>
      <td>-0.183784</td>
      <td>-0.062419</td>
      <td>-0.069071</td>
      <td>-0.064503</td>
      <td>0.014807</td>
      <td>...</td>
      <td>-0.025444</td>
      <td>0.018251</td>
      <td>0.061081</td>
      <td>-0.004296</td>
      <td>0.026799</td>
      <td>0.062157</td>
      <td>-0.003793</td>
      <td>-0.022174</td>
      <td>-0.028921</td>
      <td>-0.025606</td>
    </tr>
    <tr>
      <th>GrLivArea</th>
      <td>0.074853</td>
      <td>0.402797</td>
      <td>0.263116</td>
      <td>0.593007</td>
      <td>-0.079686</td>
      <td>0.199010</td>
      <td>0.287389</td>
      <td>0.390857</td>
      <td>0.208171</td>
      <td>-0.009640</td>
      <td>...</td>
      <td>0.247433</td>
      <td>0.330224</td>
      <td>0.009113</td>
      <td>0.020643</td>
      <td>0.101510</td>
      <td>0.170205</td>
      <td>-0.002416</td>
      <td>0.050240</td>
      <td>-0.036526</td>
      <td>0.708624</td>
    </tr>
    <tr>
      <th>BsmtFullBath</th>
      <td>0.003491</td>
      <td>0.100949</td>
      <td>0.158155</td>
      <td>0.111098</td>
      <td>-0.054942</td>
      <td>0.187599</td>
      <td>0.119470</td>
      <td>0.085310</td>
      <td>0.649212</td>
      <td>0.158678</td>
      <td>...</td>
      <td>0.175315</td>
      <td>0.067341</td>
      <td>-0.049911</td>
      <td>-0.000106</td>
      <td>0.023148</td>
      <td>0.067616</td>
      <td>-0.023047</td>
      <td>-0.025361</td>
      <td>0.067049</td>
      <td>0.227122</td>
    </tr>
    <tr>
      <th>BsmtHalfBath</th>
      <td>-0.002333</td>
      <td>-0.007234</td>
      <td>0.048046</td>
      <td>-0.040150</td>
      <td>0.117821</td>
      <td>-0.038162</td>
      <td>-0.012337</td>
      <td>0.026673</td>
      <td>0.067418</td>
      <td>0.070948</td>
      <td>...</td>
      <td>0.040161</td>
      <td>-0.025324</td>
      <td>-0.008555</td>
      <td>0.035114</td>
      <td>0.032121</td>
      <td>0.020025</td>
      <td>-0.007367</td>
      <td>0.032873</td>
      <td>-0.046524</td>
      <td>-0.016844</td>
    </tr>
    <tr>
      <th>FullBath</th>
      <td>0.131608</td>
      <td>0.198769</td>
      <td>0.126031</td>
      <td>0.550600</td>
      <td>-0.194149</td>
      <td>0.468271</td>
      <td>0.439046</td>
      <td>0.276833</td>
      <td>0.058543</td>
      <td>-0.076444</td>
      <td>...</td>
      <td>0.187703</td>
      <td>0.259977</td>
      <td>-0.115093</td>
      <td>0.035353</td>
      <td>-0.008106</td>
      <td>0.049604</td>
      <td>-0.014290</td>
      <td>0.055872</td>
      <td>-0.019669</td>
      <td>0.560664</td>
    </tr>
    <tr>
      <th>HalfBath</th>
      <td>0.177354</td>
      <td>0.053532</td>
      <td>0.014259</td>
      <td>0.273458</td>
      <td>-0.060769</td>
      <td>0.242656</td>
      <td>0.183331</td>
      <td>0.201444</td>
      <td>0.004262</td>
      <td>-0.032148</td>
      <td>...</td>
      <td>0.108080</td>
      <td>0.199740</td>
      <td>-0.095317</td>
      <td>-0.004972</td>
      <td>0.072426</td>
      <td>0.022381</td>
      <td>0.001290</td>
      <td>-0.009050</td>
      <td>-0.010269</td>
      <td>0.284108</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>-0.023438</td>
      <td>0.263170</td>
      <td>0.119690</td>
      <td>0.101676</td>
      <td>0.012980</td>
      <td>-0.070651</td>
      <td>-0.040581</td>
      <td>0.102821</td>
      <td>-0.107355</td>
      <td>-0.015728</td>
      <td>...</td>
      <td>0.046854</td>
      <td>0.093810</td>
      <td>0.041570</td>
      <td>-0.024478</td>
      <td>0.044300</td>
      <td>0.070703</td>
      <td>0.007767</td>
      <td>0.046544</td>
      <td>-0.036014</td>
      <td>0.168213</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>0.281721</td>
      <td>-0.006069</td>
      <td>-0.017784</td>
      <td>-0.183882</td>
      <td>-0.087001</td>
      <td>-0.174800</td>
      <td>-0.149598</td>
      <td>-0.037610</td>
      <td>-0.081007</td>
      <td>-0.040751</td>
      <td>...</td>
      <td>-0.090130</td>
      <td>-0.070091</td>
      <td>0.037312</td>
      <td>-0.024600</td>
      <td>-0.051613</td>
      <td>-0.014525</td>
      <td>0.062341</td>
      <td>0.026589</td>
      <td>0.031687</td>
      <td>-0.135907</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>0.040380</td>
      <td>0.352096</td>
      <td>0.190015</td>
      <td>0.427452</td>
      <td>-0.057583</td>
      <td>0.095589</td>
      <td>0.191740</td>
      <td>0.280682</td>
      <td>0.044316</td>
      <td>-0.035227</td>
      <td>...</td>
      <td>0.165984</td>
      <td>0.234192</td>
      <td>0.004151</td>
      <td>-0.006683</td>
      <td>0.059383</td>
      <td>0.083757</td>
      <td>0.024763</td>
      <td>0.036907</td>
      <td>-0.034516</td>
      <td>0.533723</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>-0.045569</td>
      <td>0.266639</td>
      <td>0.271364</td>
      <td>0.396765</td>
      <td>-0.023820</td>
      <td>0.147716</td>
      <td>0.112581</td>
      <td>0.249070</td>
      <td>0.260011</td>
      <td>0.046921</td>
      <td>...</td>
      <td>0.200019</td>
      <td>0.169405</td>
      <td>-0.024822</td>
      <td>0.011257</td>
      <td>0.184530</td>
      <td>0.095074</td>
      <td>0.001409</td>
      <td>0.046357</td>
      <td>-0.024096</td>
      <td>0.466929</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>0.085072</td>
      <td>0.070250</td>
      <td>-0.024947</td>
      <td>0.547766</td>
      <td>-0.324297</td>
      <td>0.825667</td>
      <td>0.642277</td>
      <td>0.252691</td>
      <td>0.153484</td>
      <td>-0.088011</td>
      <td>...</td>
      <td>0.224577</td>
      <td>0.228425</td>
      <td>-0.297003</td>
      <td>0.023544</td>
      <td>-0.075418</td>
      <td>-0.014501</td>
      <td>-0.032417</td>
      <td>0.005337</td>
      <td>-0.001014</td>
      <td>0.486362</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>-0.040110</td>
      <td>0.285691</td>
      <td>0.154871</td>
      <td>0.600671</td>
      <td>-0.185758</td>
      <td>0.537850</td>
      <td>0.420622</td>
      <td>0.364204</td>
      <td>0.224054</td>
      <td>-0.038264</td>
      <td>...</td>
      <td>0.226342</td>
      <td>0.213569</td>
      <td>-0.151434</td>
      <td>0.035765</td>
      <td>0.050494</td>
      <td>0.020934</td>
      <td>-0.043080</td>
      <td>0.040522</td>
      <td>-0.039117</td>
      <td>0.640409</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>-0.098672</td>
      <td>0.344997</td>
      <td>0.180403</td>
      <td>0.562022</td>
      <td>-0.151521</td>
      <td>0.478954</td>
      <td>0.371600</td>
      <td>0.373066</td>
      <td>0.296970</td>
      <td>-0.018227</td>
      <td>...</td>
      <td>0.224666</td>
      <td>0.241435</td>
      <td>-0.121777</td>
      <td>0.035087</td>
      <td>0.051412</td>
      <td>0.061047</td>
      <td>-0.027400</td>
      <td>0.027974</td>
      <td>-0.027378</td>
      <td>0.623431</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>-0.012579</td>
      <td>0.088521</td>
      <td>0.171698</td>
      <td>0.238923</td>
      <td>-0.003334</td>
      <td>0.224880</td>
      <td>0.205726</td>
      <td>0.159718</td>
      <td>0.204306</td>
      <td>0.067898</td>
      <td>...</td>
      <td>1.000000</td>
      <td>0.058661</td>
      <td>-0.125989</td>
      <td>-0.032771</td>
      <td>-0.074181</td>
      <td>0.073378</td>
      <td>-0.009551</td>
      <td>0.021011</td>
      <td>0.022270</td>
      <td>0.324413</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>-0.006100</td>
      <td>0.151972</td>
      <td>0.084774</td>
      <td>0.308819</td>
      <td>-0.032589</td>
      <td>0.188686</td>
      <td>0.226298</td>
      <td>0.125703</td>
      <td>0.111761</td>
      <td>0.003093</td>
      <td>...</td>
      <td>0.058661</td>
      <td>1.000000</td>
      <td>-0.093079</td>
      <td>-0.005842</td>
      <td>0.074304</td>
      <td>0.060762</td>
      <td>-0.018584</td>
      <td>0.071255</td>
      <td>-0.057619</td>
      <td>0.315856</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>-0.012037</td>
      <td>0.010700</td>
      <td>-0.018340</td>
      <td>-0.113937</td>
      <td>0.070356</td>
      <td>-0.387268</td>
      <td>-0.193919</td>
      <td>-0.110204</td>
      <td>-0.102303</td>
      <td>0.036543</td>
      <td>...</td>
      <td>-0.125989</td>
      <td>-0.093079</td>
      <td>1.000000</td>
      <td>-0.037305</td>
      <td>-0.082864</td>
      <td>0.054203</td>
      <td>0.018361</td>
      <td>-0.028887</td>
      <td>-0.009916</td>
      <td>-0.128578</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>-0.043825</td>
      <td>0.070029</td>
      <td>0.020423</td>
      <td>0.030371</td>
      <td>0.025504</td>
      <td>0.031355</td>
      <td>0.045286</td>
      <td>0.018796</td>
      <td>0.026451</td>
      <td>-0.029993</td>
      <td>...</td>
      <td>-0.032771</td>
      <td>-0.005842</td>
      <td>-0.037305</td>
      <td>1.000000</td>
      <td>-0.031436</td>
      <td>-0.007992</td>
      <td>0.000354</td>
      <td>0.029474</td>
      <td>0.018645</td>
      <td>0.044584</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>-0.026030</td>
      <td>0.041383</td>
      <td>0.043160</td>
      <td>0.064886</td>
      <td>0.054811</td>
      <td>-0.050364</td>
      <td>-0.038740</td>
      <td>0.061466</td>
      <td>0.062021</td>
      <td>0.088871</td>
      <td>...</td>
      <td>-0.074181</td>
      <td>0.074304</td>
      <td>-0.082864</td>
      <td>-0.031436</td>
      <td>1.000000</td>
      <td>0.051307</td>
      <td>0.031946</td>
      <td>0.023217</td>
      <td>0.010694</td>
      <td>0.111447</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>0.008283</td>
      <td>0.206167</td>
      <td>0.077672</td>
      <td>0.065166</td>
      <td>-0.001985</td>
      <td>0.004950</td>
      <td>0.005829</td>
      <td>0.011723</td>
      <td>0.140491</td>
      <td>0.041709</td>
      <td>...</td>
      <td>0.073378</td>
      <td>0.060762</td>
      <td>0.054203</td>
      <td>-0.007992</td>
      <td>0.051307</td>
      <td>1.000000</td>
      <td>0.029669</td>
      <td>-0.033737</td>
      <td>-0.059689</td>
      <td>0.092404</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>-0.007683</td>
      <td>0.003368</td>
      <td>0.038068</td>
      <td>-0.031406</td>
      <td>0.068777</td>
      <td>-0.034383</td>
      <td>-0.010286</td>
      <td>-0.029815</td>
      <td>0.003571</td>
      <td>0.004940</td>
      <td>...</td>
      <td>-0.009551</td>
      <td>-0.018584</td>
      <td>0.018361</td>
      <td>0.000354</td>
      <td>0.031946</td>
      <td>0.029669</td>
      <td>1.000000</td>
      <td>-0.006495</td>
      <td>0.004906</td>
      <td>-0.021190</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>-0.013585</td>
      <td>0.011200</td>
      <td>0.001205</td>
      <td>0.070815</td>
      <td>-0.003511</td>
      <td>0.012398</td>
      <td>0.021490</td>
      <td>-0.005965</td>
      <td>-0.015727</td>
      <td>-0.015211</td>
      <td>...</td>
      <td>0.021011</td>
      <td>0.071255</td>
      <td>-0.028887</td>
      <td>0.029474</td>
      <td>0.023217</td>
      <td>-0.033737</td>
      <td>-0.006495</td>
      <td>1.000000</td>
      <td>-0.145721</td>
      <td>0.046432</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>-0.021407</td>
      <td>0.007450</td>
      <td>-0.014261</td>
      <td>-0.027347</td>
      <td>0.043950</td>
      <td>-0.013618</td>
      <td>0.035743</td>
      <td>-0.008201</td>
      <td>0.014359</td>
      <td>0.031706</td>
      <td>...</td>
      <td>0.022270</td>
      <td>-0.057619</td>
      <td>-0.009916</td>
      <td>0.018645</td>
      <td>0.010694</td>
      <td>-0.059689</td>
      <td>0.004906</td>
      <td>-0.145721</td>
      <td>1.000000</td>
      <td>-0.028923</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>-0.084284</td>
      <td>0.351799</td>
      <td>0.263843</td>
      <td>0.790982</td>
      <td>-0.077856</td>
      <td>0.522897</td>
      <td>0.507101</td>
      <td>0.477493</td>
      <td>0.386420</td>
      <td>-0.011378</td>
      <td>...</td>
      <td>0.324413</td>
      <td>0.315856</td>
      <td>-0.128578</td>
      <td>0.044584</td>
      <td>0.111447</td>
      <td>0.092404</td>
      <td>-0.021190</td>
      <td>0.046432</td>
      <td>-0.028923</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
<p>37 rows × 37 columns</p>
</div>




```python
df.corr()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>OverallQual</th>
      <th>OverallCond</th>
      <th>YearBuilt</th>
      <th>YearRemodAdd</th>
      <th>MasVnrArea</th>
      <th>BsmtFinSF1</th>
      <th>BsmtFinSF2</th>
      <th>...</th>
      <th>WoodDeckSF</th>
      <th>OpenPorchSF</th>
      <th>EnclosedPorch</th>
      <th>3SsnPorch</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MSSubClass</th>
      <td>1.000000</td>
      <td>-0.386347</td>
      <td>-0.139781</td>
      <td>0.032628</td>
      <td>-0.059316</td>
      <td>0.027850</td>
      <td>0.040581</td>
      <td>0.022936</td>
      <td>-0.069836</td>
      <td>-0.065649</td>
      <td>...</td>
      <td>-0.012579</td>
      <td>-0.006100</td>
      <td>-0.012037</td>
      <td>-0.043825</td>
      <td>-0.026030</td>
      <td>0.008283</td>
      <td>-0.007683</td>
      <td>-0.013585</td>
      <td>-0.021407</td>
      <td>-0.084284</td>
    </tr>
    <tr>
      <th>LotFrontage</th>
      <td>-0.386347</td>
      <td>1.000000</td>
      <td>0.426095</td>
      <td>0.251646</td>
      <td>-0.059213</td>
      <td>0.123349</td>
      <td>0.088866</td>
      <td>0.193458</td>
      <td>0.233633</td>
      <td>0.049900</td>
      <td>...</td>
      <td>0.088521</td>
      <td>0.151972</td>
      <td>0.010700</td>
      <td>0.070029</td>
      <td>0.041383</td>
      <td>0.206167</td>
      <td>0.003368</td>
      <td>0.011200</td>
      <td>0.007450</td>
      <td>0.351799</td>
    </tr>
    <tr>
      <th>LotArea</th>
      <td>-0.139781</td>
      <td>0.426095</td>
      <td>1.000000</td>
      <td>0.105806</td>
      <td>-0.005636</td>
      <td>0.014228</td>
      <td>0.013788</td>
      <td>0.104160</td>
      <td>0.214103</td>
      <td>0.111170</td>
      <td>...</td>
      <td>0.171698</td>
      <td>0.084774</td>
      <td>-0.018340</td>
      <td>0.020423</td>
      <td>0.043160</td>
      <td>0.077672</td>
      <td>0.038068</td>
      <td>0.001205</td>
      <td>-0.014261</td>
      <td>0.263843</td>
    </tr>
    <tr>
      <th>OverallQual</th>
      <td>0.032628</td>
      <td>0.251646</td>
      <td>0.105806</td>
      <td>1.000000</td>
      <td>-0.091932</td>
      <td>0.572323</td>
      <td>0.550684</td>
      <td>0.411876</td>
      <td>0.239666</td>
      <td>-0.059119</td>
      <td>...</td>
      <td>0.238923</td>
      <td>0.308819</td>
      <td>-0.113937</td>
      <td>0.030371</td>
      <td>0.064886</td>
      <td>0.065166</td>
      <td>-0.031406</td>
      <td>0.070815</td>
      <td>-0.027347</td>
      <td>0.790982</td>
    </tr>
    <tr>
      <th>OverallCond</th>
      <td>-0.059316</td>
      <td>-0.059213</td>
      <td>-0.005636</td>
      <td>-0.091932</td>
      <td>1.000000</td>
      <td>-0.375983</td>
      <td>0.073741</td>
      <td>-0.128101</td>
      <td>-0.046231</td>
      <td>0.040229</td>
      <td>...</td>
      <td>-0.003334</td>
      <td>-0.032589</td>
      <td>0.070356</td>
      <td>0.025504</td>
      <td>0.054811</td>
      <td>-0.001985</td>
      <td>0.068777</td>
      <td>-0.003511</td>
      <td>0.043950</td>
      <td>-0.077856</td>
    </tr>
    <tr>
      <th>YearBuilt</th>
      <td>0.027850</td>
      <td>0.123349</td>
      <td>0.014228</td>
      <td>0.572323</td>
      <td>-0.375983</td>
      <td>1.000000</td>
      <td>0.592855</td>
      <td>0.315707</td>
      <td>0.249503</td>
      <td>-0.049107</td>
      <td>...</td>
      <td>0.224880</td>
      <td>0.188686</td>
      <td>-0.387268</td>
      <td>0.031355</td>
      <td>-0.050364</td>
      <td>0.004950</td>
      <td>-0.034383</td>
      <td>0.012398</td>
      <td>-0.013618</td>
      <td>0.522897</td>
    </tr>
    <tr>
      <th>YearRemodAdd</th>
      <td>0.040581</td>
      <td>0.088866</td>
      <td>0.013788</td>
      <td>0.550684</td>
      <td>0.073741</td>
      <td>0.592855</td>
      <td>1.000000</td>
      <td>0.179618</td>
      <td>0.128451</td>
      <td>-0.067759</td>
      <td>...</td>
      <td>0.205726</td>
      <td>0.226298</td>
      <td>-0.193919</td>
      <td>0.045286</td>
      <td>-0.038740</td>
      <td>0.005829</td>
      <td>-0.010286</td>
      <td>0.021490</td>
      <td>0.035743</td>
      <td>0.507101</td>
    </tr>
    <tr>
      <th>MasVnrArea</th>
      <td>0.022936</td>
      <td>0.193458</td>
      <td>0.104160</td>
      <td>0.411876</td>
      <td>-0.128101</td>
      <td>0.315707</td>
      <td>0.179618</td>
      <td>1.000000</td>
      <td>0.264736</td>
      <td>-0.072319</td>
      <td>...</td>
      <td>0.159718</td>
      <td>0.125703</td>
      <td>-0.110204</td>
      <td>0.018796</td>
      <td>0.061466</td>
      <td>0.011723</td>
      <td>-0.029815</td>
      <td>-0.005965</td>
      <td>-0.008201</td>
      <td>0.477493</td>
    </tr>
    <tr>
      <th>BsmtFinSF1</th>
      <td>-0.069836</td>
      <td>0.233633</td>
      <td>0.214103</td>
      <td>0.239666</td>
      <td>-0.046231</td>
      <td>0.249503</td>
      <td>0.128451</td>
      <td>0.264736</td>
      <td>1.000000</td>
      <td>-0.050117</td>
      <td>...</td>
      <td>0.204306</td>
      <td>0.111761</td>
      <td>-0.102303</td>
      <td>0.026451</td>
      <td>0.062021</td>
      <td>0.140491</td>
      <td>0.003571</td>
      <td>-0.015727</td>
      <td>0.014359</td>
      <td>0.386420</td>
    </tr>
    <tr>
      <th>BsmtFinSF2</th>
      <td>-0.065649</td>
      <td>0.049900</td>
      <td>0.111170</td>
      <td>-0.059119</td>
      <td>0.040229</td>
      <td>-0.049107</td>
      <td>-0.067759</td>
      <td>-0.072319</td>
      <td>-0.050117</td>
      <td>1.000000</td>
      <td>...</td>
      <td>0.067898</td>
      <td>0.003093</td>
      <td>0.036543</td>
      <td>-0.029993</td>
      <td>0.088871</td>
      <td>0.041709</td>
      <td>0.004940</td>
      <td>-0.015211</td>
      <td>0.031706</td>
      <td>-0.011378</td>
    </tr>
    <tr>
      <th>BsmtUnfSF</th>
      <td>-0.140759</td>
      <td>0.132644</td>
      <td>-0.002618</td>
      <td>0.308159</td>
      <td>-0.136841</td>
      <td>0.149040</td>
      <td>0.181133</td>
      <td>0.114442</td>
      <td>-0.495251</td>
      <td>-0.209294</td>
      <td>...</td>
      <td>-0.005316</td>
      <td>0.129005</td>
      <td>-0.002538</td>
      <td>0.020764</td>
      <td>-0.012579</td>
      <td>-0.035092</td>
      <td>-0.023837</td>
      <td>0.034888</td>
      <td>-0.041258</td>
      <td>0.214479</td>
    </tr>
    <tr>
      <th>TotalBsmtSF</th>
      <td>-0.238518</td>
      <td>0.392075</td>
      <td>0.260833</td>
      <td>0.537808</td>
      <td>-0.171098</td>
      <td>0.391452</td>
      <td>0.291066</td>
      <td>0.363936</td>
      <td>0.522396</td>
      <td>0.104810</td>
      <td>...</td>
      <td>0.232019</td>
      <td>0.247264</td>
      <td>-0.095478</td>
      <td>0.037384</td>
      <td>0.084489</td>
      <td>0.126053</td>
      <td>-0.018479</td>
      <td>0.013196</td>
      <td>-0.014969</td>
      <td>0.613581</td>
    </tr>
    <tr>
      <th>1stFlrSF</th>
      <td>-0.251758</td>
      <td>0.457181</td>
      <td>0.299475</td>
      <td>0.476224</td>
      <td>-0.144203</td>
      <td>0.281986</td>
      <td>0.240379</td>
      <td>0.344501</td>
      <td>0.445863</td>
      <td>0.097117</td>
      <td>...</td>
      <td>0.235459</td>
      <td>0.211671</td>
      <td>-0.065292</td>
      <td>0.056104</td>
      <td>0.088758</td>
      <td>0.131525</td>
      <td>-0.021096</td>
      <td>0.031372</td>
      <td>-0.013604</td>
      <td>0.605852</td>
    </tr>
    <tr>
      <th>2ndFlrSF</th>
      <td>0.307886</td>
      <td>0.080177</td>
      <td>0.050986</td>
      <td>0.295493</td>
      <td>0.028942</td>
      <td>0.010308</td>
      <td>0.140024</td>
      <td>0.174561</td>
      <td>-0.137079</td>
      <td>-0.099260</td>
      <td>...</td>
      <td>0.092165</td>
      <td>0.208026</td>
      <td>0.061989</td>
      <td>-0.024358</td>
      <td>0.040606</td>
      <td>0.081487</td>
      <td>0.016197</td>
      <td>0.035164</td>
      <td>-0.028700</td>
      <td>0.319334</td>
    </tr>
    <tr>
      <th>LowQualFinSF</th>
      <td>0.046474</td>
      <td>0.038469</td>
      <td>0.004779</td>
      <td>-0.030429</td>
      <td>0.025494</td>
      <td>-0.183784</td>
      <td>-0.062419</td>
      <td>-0.069071</td>
      <td>-0.064503</td>
      <td>0.014807</td>
      <td>...</td>
      <td>-0.025444</td>
      <td>0.018251</td>
      <td>0.061081</td>
      <td>-0.004296</td>
      <td>0.026799</td>
      <td>0.062157</td>
      <td>-0.003793</td>
      <td>-0.022174</td>
      <td>-0.028921</td>
      <td>-0.025606</td>
    </tr>
    <tr>
      <th>GrLivArea</th>
      <td>0.074853</td>
      <td>0.402797</td>
      <td>0.263116</td>
      <td>0.593007</td>
      <td>-0.079686</td>
      <td>0.199010</td>
      <td>0.287389</td>
      <td>0.390857</td>
      <td>0.208171</td>
      <td>-0.009640</td>
      <td>...</td>
      <td>0.247433</td>
      <td>0.330224</td>
      <td>0.009113</td>
      <td>0.020643</td>
      <td>0.101510</td>
      <td>0.170205</td>
      <td>-0.002416</td>
      <td>0.050240</td>
      <td>-0.036526</td>
      <td>0.708624</td>
    </tr>
    <tr>
      <th>BsmtFullBath</th>
      <td>0.003491</td>
      <td>0.100949</td>
      <td>0.158155</td>
      <td>0.111098</td>
      <td>-0.054942</td>
      <td>0.187599</td>
      <td>0.119470</td>
      <td>0.085310</td>
      <td>0.649212</td>
      <td>0.158678</td>
      <td>...</td>
      <td>0.175315</td>
      <td>0.067341</td>
      <td>-0.049911</td>
      <td>-0.000106</td>
      <td>0.023148</td>
      <td>0.067616</td>
      <td>-0.023047</td>
      <td>-0.025361</td>
      <td>0.067049</td>
      <td>0.227122</td>
    </tr>
    <tr>
      <th>BsmtHalfBath</th>
      <td>-0.002333</td>
      <td>-0.007234</td>
      <td>0.048046</td>
      <td>-0.040150</td>
      <td>0.117821</td>
      <td>-0.038162</td>
      <td>-0.012337</td>
      <td>0.026673</td>
      <td>0.067418</td>
      <td>0.070948</td>
      <td>...</td>
      <td>0.040161</td>
      <td>-0.025324</td>
      <td>-0.008555</td>
      <td>0.035114</td>
      <td>0.032121</td>
      <td>0.020025</td>
      <td>-0.007367</td>
      <td>0.032873</td>
      <td>-0.046524</td>
      <td>-0.016844</td>
    </tr>
    <tr>
      <th>FullBath</th>
      <td>0.131608</td>
      <td>0.198769</td>
      <td>0.126031</td>
      <td>0.550600</td>
      <td>-0.194149</td>
      <td>0.468271</td>
      <td>0.439046</td>
      <td>0.276833</td>
      <td>0.058543</td>
      <td>-0.076444</td>
      <td>...</td>
      <td>0.187703</td>
      <td>0.259977</td>
      <td>-0.115093</td>
      <td>0.035353</td>
      <td>-0.008106</td>
      <td>0.049604</td>
      <td>-0.014290</td>
      <td>0.055872</td>
      <td>-0.019669</td>
      <td>0.560664</td>
    </tr>
    <tr>
      <th>HalfBath</th>
      <td>0.177354</td>
      <td>0.053532</td>
      <td>0.014259</td>
      <td>0.273458</td>
      <td>-0.060769</td>
      <td>0.242656</td>
      <td>0.183331</td>
      <td>0.201444</td>
      <td>0.004262</td>
      <td>-0.032148</td>
      <td>...</td>
      <td>0.108080</td>
      <td>0.199740</td>
      <td>-0.095317</td>
      <td>-0.004972</td>
      <td>0.072426</td>
      <td>0.022381</td>
      <td>0.001290</td>
      <td>-0.009050</td>
      <td>-0.010269</td>
      <td>0.284108</td>
    </tr>
    <tr>
      <th>BedroomAbvGr</th>
      <td>-0.023438</td>
      <td>0.263170</td>
      <td>0.119690</td>
      <td>0.101676</td>
      <td>0.012980</td>
      <td>-0.070651</td>
      <td>-0.040581</td>
      <td>0.102821</td>
      <td>-0.107355</td>
      <td>-0.015728</td>
      <td>...</td>
      <td>0.046854</td>
      <td>0.093810</td>
      <td>0.041570</td>
      <td>-0.024478</td>
      <td>0.044300</td>
      <td>0.070703</td>
      <td>0.007767</td>
      <td>0.046544</td>
      <td>-0.036014</td>
      <td>0.168213</td>
    </tr>
    <tr>
      <th>KitchenAbvGr</th>
      <td>0.281721</td>
      <td>-0.006069</td>
      <td>-0.017784</td>
      <td>-0.183882</td>
      <td>-0.087001</td>
      <td>-0.174800</td>
      <td>-0.149598</td>
      <td>-0.037610</td>
      <td>-0.081007</td>
      <td>-0.040751</td>
      <td>...</td>
      <td>-0.090130</td>
      <td>-0.070091</td>
      <td>0.037312</td>
      <td>-0.024600</td>
      <td>-0.051613</td>
      <td>-0.014525</td>
      <td>0.062341</td>
      <td>0.026589</td>
      <td>0.031687</td>
      <td>-0.135907</td>
    </tr>
    <tr>
      <th>TotRmsAbvGrd</th>
      <td>0.040380</td>
      <td>0.352096</td>
      <td>0.190015</td>
      <td>0.427452</td>
      <td>-0.057583</td>
      <td>0.095589</td>
      <td>0.191740</td>
      <td>0.280682</td>
      <td>0.044316</td>
      <td>-0.035227</td>
      <td>...</td>
      <td>0.165984</td>
      <td>0.234192</td>
      <td>0.004151</td>
      <td>-0.006683</td>
      <td>0.059383</td>
      <td>0.083757</td>
      <td>0.024763</td>
      <td>0.036907</td>
      <td>-0.034516</td>
      <td>0.533723</td>
    </tr>
    <tr>
      <th>Fireplaces</th>
      <td>-0.045569</td>
      <td>0.266639</td>
      <td>0.271364</td>
      <td>0.396765</td>
      <td>-0.023820</td>
      <td>0.147716</td>
      <td>0.112581</td>
      <td>0.249070</td>
      <td>0.260011</td>
      <td>0.046921</td>
      <td>...</td>
      <td>0.200019</td>
      <td>0.169405</td>
      <td>-0.024822</td>
      <td>0.011257</td>
      <td>0.184530</td>
      <td>0.095074</td>
      <td>0.001409</td>
      <td>0.046357</td>
      <td>-0.024096</td>
      <td>0.466929</td>
    </tr>
    <tr>
      <th>GarageYrBlt</th>
      <td>0.085072</td>
      <td>0.070250</td>
      <td>-0.024947</td>
      <td>0.547766</td>
      <td>-0.324297</td>
      <td>0.825667</td>
      <td>0.642277</td>
      <td>0.252691</td>
      <td>0.153484</td>
      <td>-0.088011</td>
      <td>...</td>
      <td>0.224577</td>
      <td>0.228425</td>
      <td>-0.297003</td>
      <td>0.023544</td>
      <td>-0.075418</td>
      <td>-0.014501</td>
      <td>-0.032417</td>
      <td>0.005337</td>
      <td>-0.001014</td>
      <td>0.486362</td>
    </tr>
    <tr>
      <th>GarageCars</th>
      <td>-0.040110</td>
      <td>0.285691</td>
      <td>0.154871</td>
      <td>0.600671</td>
      <td>-0.185758</td>
      <td>0.537850</td>
      <td>0.420622</td>
      <td>0.364204</td>
      <td>0.224054</td>
      <td>-0.038264</td>
      <td>...</td>
      <td>0.226342</td>
      <td>0.213569</td>
      <td>-0.151434</td>
      <td>0.035765</td>
      <td>0.050494</td>
      <td>0.020934</td>
      <td>-0.043080</td>
      <td>0.040522</td>
      <td>-0.039117</td>
      <td>0.640409</td>
    </tr>
    <tr>
      <th>GarageArea</th>
      <td>-0.098672</td>
      <td>0.344997</td>
      <td>0.180403</td>
      <td>0.562022</td>
      <td>-0.151521</td>
      <td>0.478954</td>
      <td>0.371600</td>
      <td>0.373066</td>
      <td>0.296970</td>
      <td>-0.018227</td>
      <td>...</td>
      <td>0.224666</td>
      <td>0.241435</td>
      <td>-0.121777</td>
      <td>0.035087</td>
      <td>0.051412</td>
      <td>0.061047</td>
      <td>-0.027400</td>
      <td>0.027974</td>
      <td>-0.027378</td>
      <td>0.623431</td>
    </tr>
    <tr>
      <th>WoodDeckSF</th>
      <td>-0.012579</td>
      <td>0.088521</td>
      <td>0.171698</td>
      <td>0.238923</td>
      <td>-0.003334</td>
      <td>0.224880</td>
      <td>0.205726</td>
      <td>0.159718</td>
      <td>0.204306</td>
      <td>0.067898</td>
      <td>...</td>
      <td>1.000000</td>
      <td>0.058661</td>
      <td>-0.125989</td>
      <td>-0.032771</td>
      <td>-0.074181</td>
      <td>0.073378</td>
      <td>-0.009551</td>
      <td>0.021011</td>
      <td>0.022270</td>
      <td>0.324413</td>
    </tr>
    <tr>
      <th>OpenPorchSF</th>
      <td>-0.006100</td>
      <td>0.151972</td>
      <td>0.084774</td>
      <td>0.308819</td>
      <td>-0.032589</td>
      <td>0.188686</td>
      <td>0.226298</td>
      <td>0.125703</td>
      <td>0.111761</td>
      <td>0.003093</td>
      <td>...</td>
      <td>0.058661</td>
      <td>1.000000</td>
      <td>-0.093079</td>
      <td>-0.005842</td>
      <td>0.074304</td>
      <td>0.060762</td>
      <td>-0.018584</td>
      <td>0.071255</td>
      <td>-0.057619</td>
      <td>0.315856</td>
    </tr>
    <tr>
      <th>EnclosedPorch</th>
      <td>-0.012037</td>
      <td>0.010700</td>
      <td>-0.018340</td>
      <td>-0.113937</td>
      <td>0.070356</td>
      <td>-0.387268</td>
      <td>-0.193919</td>
      <td>-0.110204</td>
      <td>-0.102303</td>
      <td>0.036543</td>
      <td>...</td>
      <td>-0.125989</td>
      <td>-0.093079</td>
      <td>1.000000</td>
      <td>-0.037305</td>
      <td>-0.082864</td>
      <td>0.054203</td>
      <td>0.018361</td>
      <td>-0.028887</td>
      <td>-0.009916</td>
      <td>-0.128578</td>
    </tr>
    <tr>
      <th>3SsnPorch</th>
      <td>-0.043825</td>
      <td>0.070029</td>
      <td>0.020423</td>
      <td>0.030371</td>
      <td>0.025504</td>
      <td>0.031355</td>
      <td>0.045286</td>
      <td>0.018796</td>
      <td>0.026451</td>
      <td>-0.029993</td>
      <td>...</td>
      <td>-0.032771</td>
      <td>-0.005842</td>
      <td>-0.037305</td>
      <td>1.000000</td>
      <td>-0.031436</td>
      <td>-0.007992</td>
      <td>0.000354</td>
      <td>0.029474</td>
      <td>0.018645</td>
      <td>0.044584</td>
    </tr>
    <tr>
      <th>ScreenPorch</th>
      <td>-0.026030</td>
      <td>0.041383</td>
      <td>0.043160</td>
      <td>0.064886</td>
      <td>0.054811</td>
      <td>-0.050364</td>
      <td>-0.038740</td>
      <td>0.061466</td>
      <td>0.062021</td>
      <td>0.088871</td>
      <td>...</td>
      <td>-0.074181</td>
      <td>0.074304</td>
      <td>-0.082864</td>
      <td>-0.031436</td>
      <td>1.000000</td>
      <td>0.051307</td>
      <td>0.031946</td>
      <td>0.023217</td>
      <td>0.010694</td>
      <td>0.111447</td>
    </tr>
    <tr>
      <th>PoolArea</th>
      <td>0.008283</td>
      <td>0.206167</td>
      <td>0.077672</td>
      <td>0.065166</td>
      <td>-0.001985</td>
      <td>0.004950</td>
      <td>0.005829</td>
      <td>0.011723</td>
      <td>0.140491</td>
      <td>0.041709</td>
      <td>...</td>
      <td>0.073378</td>
      <td>0.060762</td>
      <td>0.054203</td>
      <td>-0.007992</td>
      <td>0.051307</td>
      <td>1.000000</td>
      <td>0.029669</td>
      <td>-0.033737</td>
      <td>-0.059689</td>
      <td>0.092404</td>
    </tr>
    <tr>
      <th>MiscVal</th>
      <td>-0.007683</td>
      <td>0.003368</td>
      <td>0.038068</td>
      <td>-0.031406</td>
      <td>0.068777</td>
      <td>-0.034383</td>
      <td>-0.010286</td>
      <td>-0.029815</td>
      <td>0.003571</td>
      <td>0.004940</td>
      <td>...</td>
      <td>-0.009551</td>
      <td>-0.018584</td>
      <td>0.018361</td>
      <td>0.000354</td>
      <td>0.031946</td>
      <td>0.029669</td>
      <td>1.000000</td>
      <td>-0.006495</td>
      <td>0.004906</td>
      <td>-0.021190</td>
    </tr>
    <tr>
      <th>MoSold</th>
      <td>-0.013585</td>
      <td>0.011200</td>
      <td>0.001205</td>
      <td>0.070815</td>
      <td>-0.003511</td>
      <td>0.012398</td>
      <td>0.021490</td>
      <td>-0.005965</td>
      <td>-0.015727</td>
      <td>-0.015211</td>
      <td>...</td>
      <td>0.021011</td>
      <td>0.071255</td>
      <td>-0.028887</td>
      <td>0.029474</td>
      <td>0.023217</td>
      <td>-0.033737</td>
      <td>-0.006495</td>
      <td>1.000000</td>
      <td>-0.145721</td>
      <td>0.046432</td>
    </tr>
    <tr>
      <th>YrSold</th>
      <td>-0.021407</td>
      <td>0.007450</td>
      <td>-0.014261</td>
      <td>-0.027347</td>
      <td>0.043950</td>
      <td>-0.013618</td>
      <td>0.035743</td>
      <td>-0.008201</td>
      <td>0.014359</td>
      <td>0.031706</td>
      <td>...</td>
      <td>0.022270</td>
      <td>-0.057619</td>
      <td>-0.009916</td>
      <td>0.018645</td>
      <td>0.010694</td>
      <td>-0.059689</td>
      <td>0.004906</td>
      <td>-0.145721</td>
      <td>1.000000</td>
      <td>-0.028923</td>
    </tr>
    <tr>
      <th>SalePrice</th>
      <td>-0.084284</td>
      <td>0.351799</td>
      <td>0.263843</td>
      <td>0.790982</td>
      <td>-0.077856</td>
      <td>0.522897</td>
      <td>0.507101</td>
      <td>0.477493</td>
      <td>0.386420</td>
      <td>-0.011378</td>
      <td>...</td>
      <td>0.324413</td>
      <td>0.315856</td>
      <td>-0.128578</td>
      <td>0.044584</td>
      <td>0.111447</td>
      <td>0.092404</td>
      <td>-0.021190</td>
      <td>0.046432</td>
      <td>-0.028923</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
<p>37 rows × 37 columns</p>
</div>




```python
df.rank().corr('kendall')
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-166-401834ad14e6> in <module>()
    ----> 1 df.rank().corr('kendall')
    

    /usr/local/lib/python3.5/dist-packages/pandas/core/frame.py in corr(self, method, min_periods)
       4577                         c = 1.
       4578                     elif not valid.all():
    -> 4579                         c = corrf(ac[valid], bc[valid])
       4580                     else:
       4581                         c = corrf(ac, bc)


    /usr/local/lib/python3.5/dist-packages/pandas/core/nanops.py in _kendall(a, b)
        687 
        688     def _kendall(a, b):
    --> 689         rs = kendalltau(a, b)
        690         if isinstance(rs, tuple):
        691             return rs[0]


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in kendalltau(x, y, initial_lexsort, nan_policy)
       3542 
       3543     # count exchanges
    -> 3544     exchanges = mergesort(0, n)
       3545     # compute ties in y after mergesort with counting
       3546     first = 0


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3491         length1 = length - length0
       3492         middle = offs + length0
    -> 3493         exchcnt += mergesort(offs, length0)
       3494         exchcnt += mergesort(middle, length1)
       3495         if y[perm[middle - 1]] < y[perm[middle]]:


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3491         length1 = length - length0
       3492         middle = offs + length0
    -> 3493         exchcnt += mergesort(offs, length0)
       3494         exchcnt += mergesort(middle, length1)
       3495         if y[perm[middle - 1]] < y[perm[middle]]:


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3492         middle = offs + length0
       3493         exchcnt += mergesort(offs, length0)
    -> 3494         exchcnt += mergesort(middle, length1)
       3495         if y[perm[middle - 1]] < y[perm[middle]]:
       3496             return exchcnt


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3491         length1 = length - length0
       3492         middle = offs + length0
    -> 3493         exchcnt += mergesort(offs, length0)
       3494         exchcnt += mergesort(middle, length1)
       3495         if y[perm[middle - 1]] < y[perm[middle]]:


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3491         length1 = length - length0
       3492         middle = offs + length0
    -> 3493         exchcnt += mergesort(offs, length0)
       3494         exchcnt += mergesort(middle, length1)
       3495         if y[perm[middle - 1]] < y[perm[middle]]:


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3492         middle = offs + length0
       3493         exchcnt += mergesort(offs, length0)
    -> 3494         exchcnt += mergesort(middle, length1)
       3495         if y[perm[middle - 1]] < y[perm[middle]]:
       3496             return exchcnt


    /usr/local/lib/python3.5/dist-packages/scipy/stats/stats.py in mergesort(offs, length)
       3506             else:
       3507                 temp[i] = perm[middle + k]
    -> 3508                 d = (offs + i) - (middle + k)
       3509                 k += 1
       3510             if d > 0:


    KeyboardInterrupt: 



```python
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
```


```python
#plt.bar(['a','b','c','d','e'],list(pd.value_counts(df.YrSold).values))
pd.DataFrame(pd.value_counts(df.YrSold)).plot.bar()
```


```python
df.median()
```


```python
df.dropna(how='any')
```


```python
pd.isnull(df)
```


```python

```


```python

```
