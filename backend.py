from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import random
import datetime
import hashlib
import base64
from PIL import Image
import io

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Realistic prototype data
THREAT_DATA = {
    "active_threats": 2847,
    "deepfakes_found": 156,
    "accuracy_rate": 98.7,
    "verified_sources": 45000,
    "threats_by_region": {
        "North America": 1247,
        "Europe": 892,
        "Asia": 456,
        "Other": 252
    },
    "threats_by_type": {
        "Deepfake Videos": 45,
        "AI-Generated Text": 38,
        "Synthetic Audio": 28,
        "Manipulated Images": 25,
        "Other": 20
    }
}

DETECTION_MODELS = {
    "text": {
        "name": "Linguistic Pattern Analyzer v3.2",
        "confidence": 0.94,
        "features": ["Perplexity Analysis", "Burstiness Detection", "Semantic Coherence", "GPT Fingerprinting"]
    },
    "image": {
        "name": "Pixel Forensics Engine v2.8",
        "confidence": 0.91,
        "features": ["GAN Artifact Detection", "Noise Pattern Analysis", "Compression Artifacts", "Color Space Analysis"]
    },
    "audio": {
        "name": "Spectral Analysis Core v1.9",
        "confidence": 0.89,
        "features": ["Voice Cloning Detection", "Spectral Anomalies", "Temporal Inconsistencies", "Acoustic Fingerprinting"]
    },
    "video": {
        "name": "Temporal Consistency Checker v4.1",
        "confidence": 0.92,
        "features": ["Frame-Level Analysis", "Motion Vector Analysis", "Face Swap Detection", "Temporal Artifacts"]
    }
}

def generate_realistic_analysis(content_type, content_data):
    """Generate realistic analysis results based on content type"""
    model = DETECTION_MODELS[content_type]
    
    # Generate realistic confidence score with some variance
    base_confidence = model["confidence"]
    variance = random.uniform(-0.1, 0.1)
    confidence = max(0.1, min(0.99, base_confidence + variance))
    
    # Generate realistic analysis based on content type
    analyses = {
        "text": [
            "Linguistic patterns indicate 87% probability of AI generation",
            "Perplexity score: 23.4 (threshold: 15.0)",
            "Burstiness analysis shows uniform sentence structure",
            "Semantic coherence index: 0.73 (human average: 0.85)",
            "GPT-3.5 fingerprint detected with 92% confidence"
        ],
        "image": [
            "GAN artifacts detected in 3 distinct regions",
            "Noise pattern analysis reveals synthetic generation markers",
            "Color space inconsistencies suggest AI manipulation",
            "Compression artifacts inconsistent with natural photography",
            "Face region shows 78% probability of deepfake generation"
        ],
        "audio": [
            "Spectral analysis indicates voice cloning with 84% confidence",
            "Temporal inconsistencies detected in 12% of audio segments",
            "Acoustic fingerprint matches known TTS model patterns",
            "Voice characteristics show artificial modulation",
            "Background noise patterns suggest synthetic generation"
        ],
        "video": [
            "Temporal frame analysis reveals 15 inconsistent segments",
            "Face swap artifacts detected in 8 frames",
            "Motion vector analysis shows unnatural movement patterns",
            "Lighting inconsistencies suggest post-processing manipulation",
            "Audio-visual synchronization anomalies detected"
        ]
    }
    
    # Generate digital fingerprint
    content_hash = hashlib.sha256(str(content_data).encode()).hexdigest()
    
    # Generate content verification hash (simulated)
    verification_hash = hashlib.sha256(f"{content_hash}{datetime.datetime.now().isoformat()}".encode()).hexdigest()
    
    return {
        "confidence": round(confidence * 100, 1),
        "authenticity_score": round(confidence * 100, 1),
        "analysis": analyses[content_type],
        "model_used": model["name"],
        "model_confidence": model["confidence"],
        "features_analyzed": model["features"],
        "digital_fingerprint": f"SHA256: {content_hash[:16]}...",
        "verification_hash": f"0x{verification_hash[:16]}...",
        "timestamp": datetime.datetime.now().isoformat(),
        "threat_level": "HIGH" if confidence < 0.3 else "MEDIUM" if confidence < 0.7 else "LOW",
        "recommendations": generate_recommendations(confidence, content_type)
    }

def generate_recommendations(confidence, content_type):
    """Generate realistic recommendations based on analysis"""
    if confidence < 0.3:
        return [
            "Content shows strong indicators of synthetic generation",
            "Recommend immediate verification from trusted sources",
            "Consider flagging for manual review",
            "Alert security team for potential disinformation campaign"
        ]
    elif confidence < 0.7:
        return [
            "Content shows mixed signals - requires further analysis",
            "Cross-reference with known fact-checking databases",
            "Consider additional verification methods",
            "Monitor for similar content patterns"
        ]
    else:
        return [
            "Content appears to be authentic",
            "Continue monitoring for any updates",
            "Maintain standard verification protocols",
            "No immediate action required"
        ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/intelligence')
def intelligence():
    return render_template('intelligence.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_content():
    """Analyze uploaded content"""
    try:
        data = request.get_json()
        content_type = data.get('type')
        content_data = data.get('content')
        
        if not content_type or not content_data:
            return jsonify({'error': 'Missing content type or data'}), 400
        
        if content_type not in DETECTION_MODELS:
            return jsonify({'error': 'Unsupported content type'}), 400
        
        analysis = generate_realistic_analysis(content_type, content_data)
        return jsonify(analysis)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/threats', methods=['GET'])
def get_threat_data():
    """Get current threat intelligence data"""
    return jsonify(THREAT_DATA)

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    """Get dashboard statistics"""
    dashboard_data = {
        "total_scans": random.randint(45000, 50000),
        "threats_detected": THREAT_DATA["active_threats"],
        "accuracy_rate": THREAT_DATA["accuracy_rate"],
        "last_scan": datetime.datetime.now().isoformat(),
        "system_status": "OPERATIONAL",
        "active_models": len(DETECTION_MODELS),
        "recent_detections": [
            {
                "id": f"TS-{random.randint(1000, 9999)}",
                "type": random.choice(["Deepfake Video", "AI Text", "Synthetic Audio"]),
                "confidence": round(random.uniform(0.7, 0.99), 2),
                "timestamp": (datetime.datetime.now() - datetime.timedelta(minutes=random.randint(1, 60))).isoformat(),
                "status": random.choice(["VERIFIED", "PENDING", "FLAGGED"])
            } for _ in range(10)
        ]
    }
    return jsonify(dashboard_data)

@app.route('/api/intelligence', methods=['GET'])
def get_intelligence_data():
    """Get intelligence and threat mapping data"""
    intelligence_data = {
        "geospatial_clusters": [
            {
                "region": "North America",
                "threat_count": THREAT_DATA["threats_by_region"]["North America"],
                "risk_level": "HIGH",
                "coordinates": [39.8283, -98.5795],
                "last_updated": datetime.datetime.now().isoformat()
            },
            {
                "region": "Europe",
                "threat_count": THREAT_DATA["threats_by_region"]["Europe"],
                "risk_level": "MEDIUM",
                "coordinates": [54.5260, 15.2551],
                "last_updated": datetime.datetime.now().isoformat()
            },
            {
                "region": "Asia",
                "threat_count": THREAT_DATA["threats_by_region"]["Asia"],
                "risk_level": "MEDIUM",
                "coordinates": [35.6762, 139.6503],
                "last_updated": datetime.datetime.now().isoformat()
            }
        ],
        "threat_timeline": [
            {
                "timestamp": (datetime.datetime.now() - datetime.timedelta(hours=i)).isoformat(),
                "threats_detected": random.randint(5, 25),
                "type": random.choice(["Deepfake", "AI Text", "Synthetic Audio"])
            } for i in range(24)
        ],
        "source_analysis": {
            "verified_sources": THREAT_DATA["verified_sources"],
            "suspicious_sources": random.randint(200, 500),
            "new_sources_today": random.randint(10, 50)
        }
    }
    return jsonify(intelligence_data)

@app.route('/api/reports', methods=['GET'])
def get_reports_data():
    """Get reports and analytics data"""
    reports_data = {
        "daily_report": {
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "total_scans": random.randint(1000, 2000),
            "threats_detected": random.randint(50, 150),
            "false_positives": random.randint(5, 15),
            "accuracy_rate": round(random.uniform(0.95, 0.99), 3)
        },
        "weekly_trends": [
            {
                "day": (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%A"),
                "scans": random.randint(800, 1200),
                "threats": random.randint(30, 80)
            } for i in range(7)
        ],
        "top_threat_types": THREAT_DATA["threats_by_type"],
        "performance_metrics": {
            "average_processing_time": f"{random.uniform(0.5, 2.0):.1f}s",
            "system_uptime": "99.9%",
            "api_calls_today": random.randint(5000, 10000),
            "data_processed": f"{random.randint(100, 500)}GB"
        }
    }
    return jsonify(reports_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
