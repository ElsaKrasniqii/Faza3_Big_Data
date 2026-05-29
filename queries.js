
// DataBank MongoDB Queries


// Query 1 — Mesatarja e Çmimit të Karburantit sipas Rajonit
db.fuelPrices.aggregate([
  {
    $group: {
      _id: "$Region",
      AvgFuelPrice: { $avg: "$Price" }
    }
  },
  {
    $sort: { AvgFuelPrice: -1 }
  },
  {
    $project: {
      _id: 0,
      RegionName: "$_id",
      AvgFuelPrice: { $round: ["$AvgFuelPrice", 4] }
    }
  }
]);



// Query 2 — Korrelacioni GDP Growth vs Çmimi i Karburantit
db.WorldBank_dataset.aggregate([
  {
    $match: {
      IndicatorName: "GDP growth (annual %)",
      IndicatorValue: { $ne: null }
    }
  },
  {
    $lookup: {
      from: "fuelPrices",
      let: { country: "$Country", year: "$Year" },
      pipeline: [
        {
          $addFields: {
            FuelYear: { $year: { $toDate: "$Date" } }
          }
        },
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$Country", "$$country"] },
                { $eq: ["$FuelYear", "$$year"] }
              ]
            },
            FuelType: "Petrol_Price_USD_per_Liter"
          }
        }
      ],
      as: "FuelData"
    }
  },
  {
    $match: { FuelData: { $ne: [] } }
  },
  {
    $project: {
      _id: 0,
      CountryName: "$Country",
      Year: "$Year",
      GDPGrowth: "$IndicatorValue",
      AvgFuelPrice: { $avg: "$FuelData.Price" }
    }
  },
  {
    $sort: { CountryName: 1, Year: 1 }
  },
  {
    $limit: 20
  }
]);
