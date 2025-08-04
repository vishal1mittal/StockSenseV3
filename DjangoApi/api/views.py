from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import CompanyInfo as ci
from . import RiskCalculator as rc
from . import HistoricalPerformance as hp
from . import News as nw
from . import Predictions as pr
from . import Levels as lv

@api_view(['GET'])
def getData(request, company_name):
    Htime = 0
    Ptime = 0
    Nlink = 0
    # if Login == "True":
    #     Htime = "6mo"
    #     Ptime = 28
    #     Nlink = 1
    # else:
    #     Htime = "1mo"
    #     Ptime = 7

    company_name = company_name.upper()
    CompanyDetails = ci.Info(company_name)
    risk = rc.GetRisk(CompanyDetails['Symbol'])
    history = hp.GetHistory(CompanyDetails['Symbol'], "1y")

    DailyLevels = lv.conclusive_data(CompanyDetails['Symbol'], "1d")
    WeeklyLevels = lv.conclusive_data(CompanyDetails['Symbol'], "7d")
    
    # person = [
    #     #StockInfo
    #     {
    #         "symbol": CompanyDetails['Symbol'],
    #         "companyName": CompanyDetails['Name'],
    #         "Cindustry": CompanyDetails['Industry'],
    #         "Csector": CompanyDetails['Sector'],
    #         "Cipo": CompanyDetails['IPO Year'],
    #         "risk": risk
    #     },
    #     #StockPrice
    #     hp.GetHistory(CompanyDetails['Symbol'], Htime),
    #     #news
    #     nw.NewsData(CompanyDetails['Name'], Nlink),
    #     # Future Price
    #     pr.PredictionData(CompanyDetails['Symbol'], "20y", Ptime),
    #     {
    #         "High": DailyLevels['Mean_High'],
    #         "Low": DailyLevels['Mean_Low'],
    #         "Close": DailyLevels['Mean_Close'],
    #         "Difference": DailyLevels['Difference'],
    #         "PivotPoint": DailyLevels['Pivot_Point'],
    #         "Resistance1": DailyLevels['R1'],
    #         "Resistance2": DailyLevels['R2'],
    #         "Resistance3": DailyLevels['R3'],
    #         "Support1": DailyLevels['S1'],
    #         "Support2": DailyLevels['S2'],
    #         "Support3": DailyLevels['S3']
    #     },
    #     {
    #         "High": WeeklyLevels['Mean_High'],
    #         "Low": WeeklyLevels['Mean_Low'],
    #         "Close": WeeklyLevels['Mean_Close'],
    #         "Difference": WeeklyLevels['Difference'],
    #         "PivotPoint": WeeklyLevels['Pivot_Point'],
    #         "Resistance1": WeeklyLevels['R1'],
    #         "Resistance2": WeeklyLevels['R2'],
    #         "Resistance3": WeeklyLevels['R3'],
    #         "Support1": WeeklyLevels['S1'],
    #         "Support2": WeeklyLevels['S2'],
    #         "Support3": WeeklyLevels['S3']
    #     }
    # ]
    person = {
  "symbol": "AAPL",
  "currency": "USD",
  "companyName": "Apple Inc.",
  "overview": {
    "price": 175.43,
    "change": 2.34,
    "changePercent": 1.35,
    "volume": "64.2M",
    "marketCap": "2.68T",
    "peRatio": 28.45,
    "dayRange": "172.80 - 176.90"
  },
  "historicalPerformance": {
    "dailyData": history,
    "performance": {
      "1d": 1.35,
      "1w": 2.89,
      "1m": 6.22,
      "3m": 8.45,
      "1y": 120.67
    }
  },
  "riskAnalysis": {
    "riskScore": 6.8,
    "volatility": 24.5,
    "beta": 1.2,
    "sharpeRatio": 1.45,
    "maxDrawdown": 15.2,
    "var95": 8.3
  },
  "technicalLevels": {
    "currentPrice": 175.43,
    "dailyLevels": {
      "support": [172.50, 170.25, 168.80],
      "resistance": [178.90, 181.25, 184.50]
    },
    "weeklyLevels": {
      "support": [165.00, 160.50, 155.75],
      "resistance": [185.00, 190.25, 195.50]
    },
    "indicators": {
      "rsi": 68.5,
      "macd": "Bullish",
      "trend": "Upward"
    }
  },
  "aiPredictions": {
    "monthlyPredictions": [
      { "date": "2024-01-27", "predictedPrice": 178.50, "confidence": 78, "direction": "up" },
      { "date": "2024-01-28", "predictedPrice": 179.20, "confidence": 75, "direction": "up" },
      { "date": "2024-01-29", "predictedPrice": 177.80, "confidence": 72, "direction": "down" },
      { "date": "2024-01-30", "predictedPrice": 180.10, "confidence": 70, "direction": "up" },
      { "date": "2024-01-31", "predictedPrice": 182.30, "confidence": 68, "direction": "up" },
      { "date": "2024-02-01", "predictedPrice": 181.90, "confidence": 74, "direction": "down" },
      { "date": "2024-02-02", "predictedPrice": 183.50, "confidence": 72, "direction": "up" },
      { "date": "2024-02-05", "predictedPrice": 184.20, "confidence": 69, "direction": "up" },
      { "date": "2024-02-06", "predictedPrice": 182.80, "confidence": 71, "direction": "down" },
      { "date": "2024-02-07", "predictedPrice": 185.10, "confidence": 66, "direction": "up" },
      { "date": "2024-02-08", "predictedPrice": 186.50, "confidence": 63, "direction": "up" },
      { "date": "2024-02-09", "predictedPrice": 184.90, "confidence": 67, "direction": "down" },
      { "date": "2024-02-12", "predictedPrice": 187.20, "confidence": 65, "direction": "up" },
      { "date": "2024-02-13", "predictedPrice": 188.80, "confidence": 62, "direction": "up" },
      { "date": "2024-02-14", "predictedPrice": 186.70, "confidence": 69, "direction": "down" },
      { "date": "2024-02-15", "predictedPrice": 189.40, "confidence": 61, "direction": "up" },
      { "date": "2024-02-16", "predictedPrice": 190.20, "confidence": 58, "direction": "up" },
      { "date": "2024-02-20", "predictedPrice": 188.60, "confidence": 64, "direction": "down" },
      { "date": "2024-02-21", "predictedPrice": 191.10, "confidence": 57, "direction": "up" },
      { "date": "2024-02-22", "predictedPrice": 192.50, "confidence": 55, "direction": "up" },
      { "date": "2024-02-23", "predictedPrice": 190.80, "confidence": 60, "direction": "down" },
      { "date": "2024-02-26", "predictedPrice": 185.30, "confidence": 68, "direction": "down" }
    ],
    "summary": {
      "nextDayPrediction": {
        "direction": "up",
        "confidence": 78,
        "targetPrice": 178.50,
        "reasoning": "Strong technical momentum with positive earnings sentiment"
      },
      "weeklyOutlook": {
        "direction": "up",
        "confidence": 65,
        "targetRange": "175-182",
        "keyFactors": ["Earnings beat", "Technical breakout", "Sector rotation"]
      },
      "riskFactors": [
        "Market volatility ahead of Fed meeting",
        "High valuation metrics",
        "Seasonal trading patterns"
      ]
    }
  },
  "news": [
    {
      "id": 1,
      "title": "AAPL Reports Strong Q4 Earnings",
      "summary": "Company exceeds analyst expectations with robust revenue growth and improved margins.",
      "time": "2 hours ago",
      "source": "Financial Times",
      "sentiment": "positive"
    },
    {
      "id": 2,
      "title": "Market Analysis: Tech Sector Outlook",
      "summary": "Analysts remain bullish on technology stocks despite recent market volatility.",
      "time": "4 hours ago",
      "source": "Reuters",
      "sentiment": "neutral"
    },
    {
      "id": 3,
      "title": "Regulatory Update Impacts Sector",
      "summary": "New regulations may affect operational costs but long-term outlook remains positive.",
      "time": "6 hours ago",
      "source": "Bloomberg",
      "sentiment": "negative"
    }
  ],
  "financialDocuments": {
    "keyMetrics": [
      { "label": "Revenue (TTM)", "value": "₹394.3B", "change": "+2.8%" },
      { "label": "Net Income (TTM)", "value": "₹97.0B", "change": "-2.8%" },
      { "label": "EPS (TTM)", "value": "₹6.13", "change": "-2.4%" },
      { "label": "ROE", "value": "174.6%", "change": "+8.2%" }
    ],
    "documents": [
      {
        "id": 1,
        "title": "Q4 2023 Earnings Report",
        "type": "10-K",
        "date": "2024-01-15",
        "size": "2.4 MB",
        "category": "Earnings"
      },
      {
        "id": 2,
        "title": "Annual Report 2023",
        "type": "10-K",
        "date": "2024-01-10",
        "size": "8.7 MB",
        "category": "Annual"
      },
      {
        "id": 3,
        "title": "Q3 2023 Financial Statements",
        "type": "10-Q",
        "date": "2023-10-30",
        "size": "1.8 MB",
        "category": "Quarterly"
      },
      {
        "id": 4,
        "title": "Proxy Statement 2023",
        "type": "DEF 14A",
        "date": "2023-04-15",
        "size": "3.2 MB",
        "category": "Proxy"
      }
    ]
  }
}
    return Response(person)