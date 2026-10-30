import React, { useState, useEffect } from 'react';

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Initial fetch to verify API Gateway
    fetch('/api/health')
      .then(res => res.json())
      .then(d => console.log('API Gateway Status:', d))
      .catch(err => console.error('API Gateway connection error:', err));
  }, []);

  return (
    <div className="min-h-screen bg-[#0b0f19] text-gray-100 p-6 flex flex-col items-center justify-center">
      <div className="max-w-xl text-center space-y-4">
        <div className="w-16 h-16 mx-auto rounded-2xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/20 text-white font-bold text-2xl">
          SG
        </div>
        <h1 className="text-3xl font-extrabold tracking-tight">SkillGap AI</h1>
        <p className="text-gray-400 text-sm">
          AI-Powered Skill Gap Analyzer & Intelligent Career Acceleration Agent.
        </p>
        <div className="p-4 rounded-xl bg-gray-900 border border-gray-800 text-xs text-left space-y-2">
          <p className="text-emerald-400 font-semibold">✓ API Gateway & Fallback Scoring Engine Ready</p>
          <p className="text-indigo-300">✓ 5-Factor Weighted Recommender (Academic 30%, Career 25%, Financial 20%, Skill 15%, Preference 10%)</p>
          <p className="text-gray-400">✓ Open <a href="http://localhost:5000" className="underline text-indigo-400 font-bold">http://localhost:5000</a> to view the complete production UI dashboard.</p>
        </div>
      </div>
    </div>
  );
}

